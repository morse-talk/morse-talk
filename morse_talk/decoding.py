"""
Functions to decode messages
"""

#    Copyright (C) 2015 by
#    Himanshu Mishra <himanshu2014iit@gmail.com>
#    All rights reserved.
#    GNU license.

import encoding

__all__ = ['decode']

def decode(code, encoding_type='default'):
    """Converts a string of morse code into English message

    The encoded message can also be decoded using the same morse chart
    backwards.

    """
    reversed_morsetab = {symbol: character for character,
                         symbol in getattr(encoding, 'morsetab').items()}

    if encoding_type == 'default':
        message = [reversed_morsetab[i] for i in code.split()]

        # For spacing the words
        letters = 0
        words = 0
        index = {}

        for i in range(0, len(code)):
            if code[i: i+3] == '   ':
                    if code[i: i+7] == '       ':
                            words += 1
                            letters += 1
                            index[words] = letters
                    elif code[i+4] and code[i-1] != ' ':  # Check for '   '
                        letters += 1

        count = 0
        for word, letter in index.items():
            message.insert(letter + count, ' ')
            count += 1
        return ''.join(message)

    if encoding == 'binary':
        return ('Sorry, but it seems that binary encodings can have multiple'
                ' messages. So for now, we couldn\'t show even one of them.')
