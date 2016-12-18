#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some tools to create Morse Code audible message

Some ideas was taken from
https://github.com/zacharydenton/wavebender/blob/master/wavebender/
"""
import sys
from math import pi, sin
import wave
import struct
from itertools import count, islice
from morse_talk.utils import (FREQUENCY, WPM, FRAMERATE, AMPLITUDE, WORD, SECONDS_PER_DOT)
from morse_talk.utils import (samples_nb, _seconds_per_dot, _limit_value)
from morse_talk.encoding import _encode_binary

BITS = 16
CHANNELS = 2

try:
    from itertools import zip_longest
except ImportError:
    from itertools import imap
    from itertools import izip
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
    return islice(izip(*(imap(sum, izip(*channel)) for channel in channels)), nsamples)


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
    omega = 2.0 * pi * float(frequency)
    sine = sin(omega * (float(i) / float(framerate)))
    return float(amplitude) * sine


def generate_wave(message, wpm=WPM, framerate=FRAMERATE, skip_frame=0, amplitude=AMPLITUDE, frequency=FREQUENCY, word_ref=WORD):
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
    lst_bin = _encode_binary(message)
    if amplitude > 1.0:
        amplitude = 1.0
    if amplitude < 0.0:
        amplitude = 0.0
    seconds_per_dot = _seconds_per_dot(word_ref)  # =1.2
    for i in count(skip_frame):
        bit = morse_bin(i=i, lst_bin=lst_bin, wpm=wpm, framerate=framerate, default_value=0.0, seconds_per_dot=seconds_per_dot)
        sine = sine_wave(i=i, frequency=frequency, framerate=framerate, amplitude=amplitude)
        yield sine * bit


def morse_bin(i, lst_bin, wpm=WPM, framerate=FRAMERATE, default_value=0.0, seconds_per_dot=1.2):
    """
    Returns value of a morse bin list at a given framerate  and code speed (wpm)
    for a given sample i
    """
    try:
        return lst_bin[int(float(wpm) * float(i) / (seconds_per_dot * float(framerate)))]
    except IndexError:
        return default_value


def calculate_wave(i, lst_bin, wpm=WPM, frequency=FREQUENCY, framerate=FRAMERATE, amplitude=AMPLITUDE, seconds_per_dot=SECONDS_PER_DOT):
    """
    Returns product of a sin wave and morse code (dit, dah, silent)
    """
    bit = morse_bin(i=i, lst_bin=lst_bin, wpm=wpm, framerate=framerate,
                    default_value=0.0, seconds_per_dot=seconds_per_dot)
    sine = sine_wave(i=i, frequency=frequency, framerate=framerate, amplitude=amplitude)
    return bit * sine


def preview_wave(message, wpm=WPM, frequency=FREQUENCY, framerate=FRAMERATE, amplitude=AMPLITUDE, word_ref=WORD):
    """
    Listen (preview) wave

    sounddevice is required http://python-sounddevice.readthedocs.org/
    $ pip install sounddevice
    """
    samp_nb = samples_nb(message=message, wpm=wpm, framerate=framerate, word_spaced=False)
    import sounddevice as sd
    lst_bin = _encode_binary(message)
    amplitude = _limit_value(amplitude)
    seconds_per_dot = _seconds_per_dot(word_ref)  # 1.2
    a = [calculate_wave(i, lst_bin, wpm, frequency, framerate, amplitude, seconds_per_dot)
         for i in range(samp_nb)]
    sd.play(a, framerate, blocking=True)


def main():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    main()
