#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some Morse code functions

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.

"""

WORD = 'PARIS'  # Reference word for code speed
# http://www.kent-engineers.com/codespeed.htm

WPM = 15  # default code speed
FRAMERATE = 44100 / 4  # default framerate
FREQUENCY = 750  # default sound frequency
AMPLITUDE = 0.5

import morse_talk as mtalk
from itertools import count
import math

def _repeat_word(word, N, word_space=" "):
    """
    Return a repeated string

    >>> word = "PARIS"

    >>> _repeat_word(word, 5)
    'PARIS PARIS PARIS PARIS PARIS'

    >>> _repeat_word(word, 5, word_space="")
    'PARISPARISPARISPARISPARIS'
    """
    message = (word_space + word) * N
    message = message[len(word_space):]
    return message

def mlength(message, N=1, word_spaced=True):
    """
    Returns Morse length

    >>> message = "PARIS"
    >>> mlength(message)
    50
    >>> mlength(message, 5)
    250
    """
    message = _repeat_word(message, N)
    if word_spaced:
        message = message + " E"
    lst_bin = mtalk.encoding._encode_binary(message)
    N = len(lst_bin)
    if word_spaced:
        N -= 1 # E is one "dit" so we remove it
    return N

def wpm_to_duration(wpm, output='timedelta', word=WORD):
    """
    Convert from WPM (word per minutes) to 
    element duration

    Parameters
    ----------
    wpm : int or float - word per minute
    output : String - type of output
        'timedelta'
        'float'
        'decimal'
    word : string - reference word (PARIS by default)

    Returns
    -------
    duration : timedelta or float or decimal.Decimal - duration of an element

    >>> wpm_to_duration(5, output='decimal')
    Decimal('240')

    >>> wpm_to_duration(5, output='float')
    240.0

    >>> wpm_to_duration(5, output='timedelta')
    datetime.timedelta(0, 0, 240000)

    >>> wpm_to_duration(15, output='decimal')
    Decimal('80')

    >>> wpm_to_duration(13, output='decimal')
    Decimal('92.30769230769230769230769231')

    >>> wpm_to_duration(5.01, output='timedelta')
    datetime.timedelta(0, 0, 239521)
    """
    N = mlength(word) * wpm
    output = output.lower()
    allowed_output = ['decimal', 'float', 'timedelta']
    if output == 'decimal':
        import decimal
        duration = 60 * 1000 / decimal.Decimal(N)
    elif output == 'float':
        duration = 60 * 1000 / float(N)
    elif output == 'timedelta':
        import datetime
        duration = datetime.timedelta(seconds=(60 / float(N)))
    else:
        raise NotImplementedError("output must be in %s" % allowed_output)
    return duration

def duration(message, wpm, output='timedelta', word_ref=WORD, word_spaced=False):
    """
    Calculate duration to send a message at a given code speed 
    (calculated using reference word PARIS)

    Parameters
    ----------
    word : string
    wpm : int or float - word per minute
    output : String - type of output
        'timedelta'
        'float'
        'decimal'
    word : string - reference word (PARIS by default)
    word_spaced : bool - calculate with spaces between 2 words (default is False)

    Returns
    -------
    duration : timedelta or float or decimal.Decimal - duration of the word `word`

    >>> duration(_repeat_word('PARIS', 5), 5, word_spaced=True)
    datetime.timedelta(0, 60)

    >>> duration('PARIS', 15)
    datetime.timedelta(0, 3, 440000)

    >>> duration('SOS', 15)
    datetime.timedelta(0, 2, 160000)
    """
    elt_duration = wpm_to_duration(wpm, output=output)
    word_length = mlength(message, word_spaced=word_spaced)
    return word_length * elt_duration

def samples_nb(message, wpm, framerate=FRAMERATE, word_spaced=False):
    """
    Calculate the number of samples for a given word at a given framerate (samples / seconds)

    >>> samples_nb('SOS', 15)
    23814
    """
    return int(duration(message, wpm, output='float', word_spaced=word_spaced) / 1000.0 * framerate)

def sine_wave(i, frequency=FREQUENCY, framerate=FRAMERATE, amplitude=AMPLITUDE):
    """
    Returns value of a sine wave at a given frequency and framerate
    for a given sample i
    """
    if amplitude > 1.0: amplitude = 1.0
    if amplitude < 0.0: amplitude = 0.0
    sine = math.sin(2.0 * math.pi * float(frequency) * (float(i) / float(framerate)))
    return float(amplitude) * sine

def morse_bin(i, lst_bin, wpm, framerate=FRAMERATE, default_value=0.0, seconds_per_dot=1.2):
    """
    Returns value of a morse bin list at a given framerate  and code speed (wpm)
    for a given sample i
    """
    try:
        return lst_bin[int(float(wpm) * float(i) / (seconds_per_dot * float(framerate)))]
    except IndexError:
        return default_value   

def generate_bin(message, wpm, framerate=FRAMERATE, word_spaced=False, skip_frame=0, amplitude=1.0, frequency=FREQUENCY, word_ref=WORD):
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
    seconds_per_dot = 60 / mlength(word_ref) # 1.2
    for i in count(skip_frame):
        bit = morse_bin(i=i, lst_bin=lst_bin, wpm=wpm, framerate=framerate, default_value=0.0, seconds_per_dot=seconds_per_dot)
        sine = sine_wave(i=i, frequency=frequency, framerate=framerate, amplitude=amplitude)
        yield sine * bit

def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()