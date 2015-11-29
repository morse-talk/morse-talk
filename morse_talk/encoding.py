"""
Functions to encode strings
"""

#    Copyright (C) 2015 by
#    Himanshu Mishra <himanshu2014iit@gmail.com>
#    All rights reserved.
#    GNU GPL v2 license.

__all__ = ['encode']

import collections

morsetab = collections.OrderedDict([
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),
    ('1', '.----'),
    ('2', '..---'),
    ('3', '...--'),
    ('4', '....-'),
    ('5', '.....'),
    ('6', '-....'),
    ('7', '--...'),
    ('8', '---..'),
    ('9', '----.'),
    (' ', ' '),
    (',', '--..--'),
    ('.', '.-.-.-'),
    ('?', '..--..'),
    (';', '-.-.-.'),
    (':', '---...'),
    ("'", '.----.'),
    ('-', '-....-'),
    ('/', '-..-.'),
    ('(', '-.--.-'),
    (')', '-.--.-'),
    ('_', '..--.-')
])

def _encode_morse(message):
    """
    >>> message = "SOS"
    >>> _encode_morse(message)
    ['...', '---', '...']
    """
    return [morsetab.get(c.upper(), '?') for c in message]

def _encode_binary(message, on=1, off=0):
    """
    >>> message = "SOS"
    >>> _encode_binary(message)
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1]

    >>> _encode_binary(message, on='1', off='0')
    ['1', '0', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1']
    """
    l = _encode_morse(message)
    s = ' '.join(l)
    l = list(s)
    bin_conv = { '.': [on], '-': [on]*3, ' ': [off]}
    l = map(lambda symb: [off] + bin_conv[symb], l)
    lst = [item for sublist in l for item in sublist] # flatten list
    return lst[1:]

def encode(message, encoding_type='default', letter_sep = ' '*3, strip=True):
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

    >>> message = "SOS"
    >>> encode(message)
    '...   ---   ...'

    Parameters
    ----------
    message : String

    encoding : Type of encoding
        Supported types are default(morse) and binary.

    Returns
    -------
    encoded_message : String
    """
    if strip:
        message = message.strip()  # No trailing or leading spaces

    encoding_type = encoding_type.lower()
    allowed_encoding_type = ['default', 'binary']

    if encoding_type == 'default':
        return letter_sep.join(_encode_morse(message))

    elif encoding_type == 'binary':
        return ''.join(_encode_binary(message, on='1', off='0'))

    else:
        raise NotImplementedError("encoding_type must be in %s" % allowed_encoding_type)

def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
