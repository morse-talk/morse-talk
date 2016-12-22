#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Morse Binary CLI plotter

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.

Usage:
$ mplot -m "MORSE CODE"
"""

import argparse

import matplotlib.pyplot as plt

import morse_talk.plot as mplot
from morse_talk.utils import WORD
from morse_talk.utils import display, _get_speed


def main():
    parser = argparse.ArgumentParser(prog="mplot", description='Plot morse code')
    parser.add_argument('-m', '--message', help='Message', default='SOS')
    parser.add_argument('-d', '--duration', help='Element duration', default=None, type=float)
    parser.add_argument('-s', '--speed', help="Speed in wpm (Words per minutes)", default=None, type=float)
    parser.add_argument('-w', '--word-ref', help="Reference word", default=WORD)
    args = parser.parse_args()

    message = args.message
    element_duration = args.duration
    wpm = args.speed
    word_ref = args.word_ref

    element_duration, wpm = _get_speed(element_duration, wpm)

    display(message, wpm, element_duration, word_ref)

    mplot.plot(message, element_duration)
    plt.show()


if __name__ == '__main__':
    main()
