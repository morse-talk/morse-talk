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
from utils import generate_bin, samples_nb, FREQUENCY, WPM, FRAMERATE
import morse_talk as mtalk

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

def main():
    parser = argparse.ArgumentParser(prog="wavebender")
    parser.add_argument('-c', '--channels', help="Number of channels to produce", default=2, type=int)
    parser.add_argument('-b', '--bits', help="Number of bits in each sample", choices=(16,), default=16, type=int)
    parser.add_argument('-r', '--rate', help="Sample rate in Hz", default=FRAMERATE, type=int)
    parser.add_argument('-a', '--amplitude', help="Amplitude of the wave on a scale of 0.0-1.0.", default=0.5, type=float)
    parser.add_argument('-f', '--frequency', help="Frequency of the wave in Hz", default=FREQUENCY, type=float)
    parser.add_argument('--filename', help="The file to generate.", default="out.wav")
    parser.add_argument('-s', '--speed', help="Speed in wpm (Words per minutes)", default=WPM, type=float)
    parser.add_argument('-m', '--message', help="Message", default="SOS")
    args = parser.parse_args()

    # each channel is defined by infinite functions which are added to produce a sample.
    framerate = args.rate
    wpm = args.speed
    message = args.message

    print("text : %r" % message)
    print("morse: %s" % mtalk.encode(message))
    print("bin  : %s" % mtalk.encode(message, encoding_type='binary'))

    channels = ((generate_bin(message=message, wpm=wpm, framerate=framerate, word_spaced=False, skip_frame=0),) for i in range(args.channels))

    # convert the channel functions into waveforms
    samp_nb = samples_nb(message=message, wpm=wpm, framerate=framerate, word_spaced=False)
    samples = compute_samples(channels, samp_nb)

    # write the samples to a file
    if args.filename == '-':
        filename = stdout
    else:
        filename = args.filename
    write_wavefile(filename, samples, samp_nb, args.channels, args.bits // 8, args.rate)

if __name__ == "__main__":
    main()