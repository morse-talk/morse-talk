"""
Functions to encode strings
"""

#    Copyright (C) 2015 by
#    Himanshu Mishra <himanshu2014iit@gmail.com>
#    All rights reserved.
#    GNU license.

__all__ = ['encode']

morsetab = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-', 
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
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


def encode(message, encoding_type='default', letter_sep = '   '):
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
        return letter_sep.join([morsetab.get(c.upper(), '?') for c in message])

    elif encoding_type == 'binary':
        bin_conv = { '.': '1', '-': '111', ' ': '0'}
        #return ''.join([bin_conv.get(i, '?') for i in encode(message, letter_sep = ' ')])
        return ''.join(["0" + bin_conv.get(i, '?') for i in encode(message, letter_sep = ' ')])[1:]
