"""
Functions to encode and decode strings
"""

#    Copyright (C) 2015 by
#    Himanshu Mishra <himanshu2014iit@gmail.com>
#    All rights reserved.
#    GNU license.

__all__ = ['encode', 'decode']

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


def encode(message, encoding='default'):
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

    if encoding == 'default':
        char = list(message)  # char is a list of all the characters in message
        encoded_message = []
        words_len_list = [len(i) for i in message.split()]  # list of length
                                        # of words in order of its occurence

        checkpoints = []
        checkpoints.append(words_len_list[0])
        for i in range(1, len(words_len_list)):
            checkpoints.append(checkpoints[i-1] + words_len_list[i])

        counter = 0
        for character in char:
            try:
                encoded_message.append(morsetab[character])

                if counter in checkpoints:
                    encoded_message.append('       ')  # end of a word
                else:
                    encoded_message.append('   ')  # end of a letter
            except KeyError:
                print("WARNING: Unsupported characters in the string")

        return ''.join(encoded_message).rstrip('   ')

    elif encoding == 'binary':
        encoded_message = encode(message)
        converted = []
        for i in encoded_message:
            if i == '.':
                converted.append('1')
            if i == '-':
                converted.append('111')
            if i == ' ':
                converted.append('0')
        return ''.join(converted).rstrip('000')

def decode(code, encoding='default'):
    """Converts a string of morse code into English message

    The encoded message can also be decoded using the same morse chart
    backwards.

    """
    reversed_morsetab = {symbol : character for character, symbol in morsetab.items()}

    if encoding == 'default':
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
                    elif code[i+4] and code[i-1] != ' ':
                        letters += 1

        count = 0
        for word, letter in index.items():
            message.insert(letter + count , ' ')
            count += 1
        return ''.join(message)

    if encoding == 'binary':
        return ('Sorry, but it seems that binary encodings can have multiple'
                ' messages. So for now, we couldn\'t show even one of them.')
