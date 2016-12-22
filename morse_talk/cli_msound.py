#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Morse Binary CLI sound generator

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.

Usage:
$ msound -m "MORSE CODE"
"""

import argparse
import sys

from morse_talk.utils import (FRAMERATE, AMPLITUDE, FREQUENCY, WORD)
from morse_talk.utils import (_get_speed, display, samples_nb)

from morse_talk.sound import (BITS, CHANNELS)
from morse_talk.sound import (preview_wave, compute_samples,
                              generate_wave, write_wavefile)


def main():
    parser = argparse.ArgumentParser(prog="msound", description='Create or listen morse code sound')
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
    parser.add_argument('-l', '--loop', dest='loop', action='store_true')
    args = parser.parse_args()

    message = args.message
    element_duration = args.duration
    wpm = args.speed
    framerate = args.rate
    amplitude = args.amplitude
    word_ref = args.word_ref

    element_duration, wpm = _get_speed(element_duration, wpm)

    display(message, wpm, element_duration, word_ref)

    if args.filename == '':  # preview
        preview_wave(message, wpm, args.frequency, framerate, amplitude, word_ref)
        while(args.loop):
            message_with_space = " " + message
            preview_wave(message_with_space, wpm, args.frequency, framerate, amplitude, word_ref)
    else:
        channels = ((generate_wave(message=message, wpm=wpm, framerate=framerate, skip_frame=0),) for i in range(args.channels))

        # convert the channel functions into waveforms
        samp_nb = samples_nb(message=message, wpm=wpm, framerate=framerate, word_spaced=False)
        samples = compute_samples(channels, samp_nb)

        if args.filename == '-':  # write to console
            filename = sys.stdout
            write_wavefile(filename, samples, samp_nb, args.channels, args.bits // 8, args.rate)
        else:  # write the samples to a .wav file
            filename = args.filename

        write_wavefile(filename, samples, samp_nb, args.channels, args.bits // 8, args.rate)


if __name__ == "__main__":
    main()
