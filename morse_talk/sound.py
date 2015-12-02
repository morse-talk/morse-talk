#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some tools to create Morse Code audible message

Some ideas was taken from
https://github.com/zacharydenton/wavebender/blob/master/wavebender/
"""
import sys
import math
import wave
import struct
import random
import argparse
from itertools import count, islice
from morse_talk.utils import (FREQUENCY, WPM, FRAMERATE, AMPLITUDE, WORD)
from morse_talk.utils import (samples_nb, mlength, display, _get_speed,
        _seconds_per_dot, _limit_value)
import morse_talk as mtalk

BITS = 16
CHANNELS = 2

try:
    from itertools import zip_longest
except ImportError:
    from itertools import imap as map
    from itertools import izip as zip
    from itertools import izip_longest as zip_longest

try:
    stdout = sys.stdout.buffer
except AttributeError:
    stdout = sys.stdout

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

def compute_samples(channels, nsamples=None):
    '''
    create a generator which computes the samples.
    essentially it creates a sequence of the sum of each function in the channel
    at each sample in the file for each channel.
    '''
    return islice(zip(*(map(sum, zip(*channel)) for channel in channels)), nsamples)

def write_wavefile(f, samples, nframes=None, nchannels=2, sampwidth=2, framerate=44100, bufsize=2048):
    "Write samples to a wavefile."
    if nframes is None:
        nframes = 0

    w = wave.open(f, 'wb')
    w.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

    # split the samples into chunks (to reduce memory consumption and improve performance)
    for chunk in grouper(bufsize, samples):
        frames = b''.join(b''.join(struct.pack('h', int(max_amplitude * sample)) for sample in channels) for channels in chunk if channels is not None)
        w.writeframesraw(frames)
    
    w.close()

def sine_wave(i, frequency=FREQUENCY, framerate=FRAMERATE, amplitude=AMPLITUDE):
    """
    Returns value of a sine wave at a given frequency and framerate
    for a given sample i
    """
    #if amplitude > 1.0: amplitude = 1.0
    #if amplitude < 0.0: amplitude = 0.0
    sine = math.sin(2.0 * math.pi * float(frequency) * (float(i) / float(framerate)))
    return float(amplitude) * sine


def generate_wave(message, wpm, framerate=FRAMERATE, word_spaced=False, skip_frame=0, amplitude=AMPLITUDE, frequency=FREQUENCY, word_ref=WORD):
    """
    Generate binary Morse code of message at a given code speed wpm and framerate

    Parameters
    ----------
    word : string
    wpm : int or float - word per minute
    framerate : nb of samples / seconds
    word_spaced : bool - calculate with spaces between 2 words (default is False)
    skip_frame : int - nb of frame to skip

    Returns
    -------
    value : float

    """
    lst_bin = mtalk.encoding._encode_binary(message)
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    seconds_per_dot = _seconds_per_dot(word_ref) # =1.2
    for i in count(skip_frame):
        bit = morse_bin(i=i, lst_bin=lst_bin, wpm=wpm, framerate=framerate, default_value=0.0, seconds_per_dot=seconds_per_dot)
        sine = sine_wave(i=i, frequency=frequency, framerate=framerate, amplitude=amplitude)
        yield sine * bit

def morse_bin(i, lst_bin, wpm, framerate=FRAMERATE, default_value=0.0, seconds_per_dot=1.2):
    """
    Returns value of a morse bin list at a given framerate  and code speed (wpm)
    for a given sample i
    """
    try:
        return lst_bin[int(float(wpm) * float(i) / (seconds_per_dot * float(framerate)))]
    except IndexError:
        return default_value   

def calculate_wave(i, lst_bin, wpm, frequency, framerate, amplitude, seconds_per_dot):
    """
    Returns product of a sin wave and morse code (dit, dah, silent)
    """
    bit = morse_bin(i=i, lst_bin=lst_bin, wpm=wpm, framerate=framerate, 
            default_value=0.0, seconds_per_dot=seconds_per_dot)
    sine = sine_wave(i=i, frequency=frequency, framerate=framerate, amplitude=amplitude)
    return bit * sine

def preview_wave(message, wpm, samp_nb, frequency, framerate, amplitude, word_ref=WORD):
    """
    Listen (preview) wave

    sounddevice is required http://python-sounddevice.readthedocs.org/
    $ pip install sounddevice
    """
    import sounddevice as sd
    omega = 2 * math.pi * frequency
    lst_bin = mtalk.encoding._encode_binary(message)
    amplitude = _limit_value(amplitude)
    seconds_per_dot = 60 / mlength(word_ref) # 1.2
    a = [calculate_wave(i, lst_bin, wpm, frequency, framerate, amplitude, seconds_per_dot)
        for i in range(samp_nb)]
    sd.play(a, framerate, blocking=True)

def main():
    parser = argparse.ArgumentParser(prog="sound")
    parser.add_argument('-c', '--channels', help="Number of channels to produce", default=CHANNELS, type=int)
    parser.add_argument('-b', '--bits', help="Number of bits in each sample", choices=(BITS,), default=BITS, type=int)
    parser.add_argument('-r', '--rate', help="Sample rate in Hz", default=FRAMERATE, type=int)
    parser.add_argument('-a', '--amplitude', help="Amplitude of the wave on a scale of 0.0-1.0.", default=AMPLITUDE, type=float)
    parser.add_argument('-f', '--frequency', help="Frequency of the wave in Hz", default=FREQUENCY, type=float)
    parser.add_argument('-o', '--filename', help="The file to generate.", default='')
    parser.add_argument('-m', '--message', help='Message', default='SOS')
    parser.add_argument('-d', '--duration', help='Element duration', default=None, type=float)
    parser.add_argument('-s', '--speed', help="Speed in wpm (Words per minutes)", default=None, type=float)
    parser.add_argument('-w', '--word-ref', help="Reference word", default=WORD)
    args = parser.parse_args()

    message = args.message
    element_duration = args.duration
    wpm = args.speed
    framerate = args.rate
    amplitude = args.amplitude
    word_ref = args.word_ref

    element_duration, wpm = _get_speed(element_duration, wpm)

    display(message, wpm, element_duration, word_ref)

    channels = ((generate_wave(message=message, wpm=wpm, framerate=framerate, word_spaced=False, skip_frame=0),) for i in range(args.channels))

    # convert the channel functions into waveforms
    samp_nb = samples_nb(message=message, wpm=wpm, framerate=framerate, word_spaced=False)
    samples = compute_samples(channels, samp_nb)
    
    if args.filename == '': # preview
        preview_wave(message, wpm, samp_nb, args.frequency, framerate, amplitude)
    elif args.filename == '-': # write to console
        filename = stdout
        write_wavefile(filename, samples, samp_nb, args.channels, args.bits // 8, args.rate)
    else: # write the samples to a .wav file
        filename = args.filename
        write_wavefile(filename, samples, samp_nb, args.channels, args.bits // 8, args.rate)

if __name__ == "__main__":
    main()