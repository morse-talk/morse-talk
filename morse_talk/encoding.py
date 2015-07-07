"""
Functions to encode strings
"""

#    Copyright (C) 2015 by
#    Himanshu Mishra <himanshu2014iit@gmail.com>
#    All rights reserved.
#    MIT license.

__all__ = ['encode']

morsetab = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
}


def encode(message, encoding_type='default'):
    """Converts a string of message into morse

    Two types of marks are there. One is short mark, dot(.) or "dit" and
    other is long mark, dash(-) or "dah". After every dit or dah, there is
    a one dot duration or one unit log gap.

    Between every letter, there is a short gap (three units long).
    Between every word, there is a medium gap (seven units long).

    When encoding is changed to binary, the short mark(dot) is denoted by 1
    and the long mark(dash) is denoted by 111. The intra character gap between
    letters is represented by 0.

    The short gap is represented by 000 and the medium gap by 0000000.

    Parameters
    ----------
    message : String

    encoding : Type of encoding
        Supported types are default(morse) and binary.

    Returns
    -------
    encoded_message : String

    """
    message = message.strip()  # No trailing or leading spaces

    if encoding_type == 'default':
        letter_sep = '   '
        return letter_sep.join([morsetab.get(c, '?') for c in message])

    elif encoding_type == 'binary':
        bin_conv = { '.': '1', '-': '111', ' ': '0'}
        return ''.join([bin_conv.get(i, '?') for i in encode(message)])
