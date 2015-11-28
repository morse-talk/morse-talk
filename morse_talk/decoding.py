"""
Functions to decode messages
"""

#    Copyright (C) 2015 by
#    Himanshu Mishra <himanshu2014iit@gmail.com>
#    All rights reserved.
#    GNU license.

from . import encoding
from encoding import morsetab, encode
__all__ = ['decode']

binary_lookup = {encode(key, encoding_type='binary'): key for key, value in morsetab.items()}

def decode(code, encoding_type='default'):
    """Converts a string of morse code into English message

    The encoded message can also be decoded using the same morse chart
    backwards.

    """
    reversed_morsetab = {symbol: character for character,
                         symbol in list(getattr(encoding, 'morsetab').items())}

    if encoding_type == 'default':

        # For spacing the words
        letters = 0
        words = 0
        index = {}

        for i in range(len(code)):
            if code[i: i+3] == '   ':
                    if code[i: i+7] == '       ':
                            words += 1
                            letters += 1
                            index[words] = letters
                    elif code[i+4] and code[i-1] != ' ':  # Check for '   '
                        letters += 1

        message = [reversed_morsetab[i] for i in code.split()]
        for i, (word, letter) in enumerate(list(index.items())):
            message.insert(letter + i, ' ')
        return ''.join(message)

    if encoding_type == 'binary':
        lst = map(lambda word: word.split("0"*3), code.split("0"*7))
        # list of list of character (each sub list being a word)
        for i, word in enumerate(lst):
            for j, bin_letter in enumerate(word):
                lst[i][j] = binary_lookup[bin_letter]
            lst[i] = "".join(lst[i])
        s = " ".join(lst)
        return s
