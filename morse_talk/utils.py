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
from morse_talk.encoding import (_split_message, _encode_binary, _encode_to_binary_string)

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
    lst_bin = _encode_binary(message)
    N = len(lst_bin)
    if word_spaced:
        N -= 1 # E is one "dit" so we remove it
    return N

def wpm_to_duration(wpm, output='timedelta', word_ref=WORD):
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
    word_ref : string - reference word (PARIS by default)

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
    N = mlength(word_ref) * wpm
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
    elt_duration = wpm_to_duration(wpm, output=output, word_ref=word_ref)
    word_length = mlength(message, word_spaced=word_spaced)
    return word_length * elt_duration

def samples_nb(message, wpm, framerate=FRAMERATE, word_spaced=False):
    """
    Calculate the number of samples for a given word at a given framerate (samples / seconds)

    >>> samples_nb('SOS', 15)
    23814
    """
    return int(duration(message, wpm, output='float', word_spaced=word_spaced) / 1000.0 * framerate)

def _seconds_per_dot(word_ref=WORD):
    """
    >>> _seconds_per_dot('PARIS')
    1.2
    """
    return 60 / mlength(word_ref) # 1.2 with 'PARIS'

def _get_speed(element_duration, wpm, word_ref=WORD):
    """
    Returns
        element duration when element_duration and/or code speed is given
        wpm    

    >>> _get_speed(0.2, None)
    (0.2, 5.999999999999999)

    >>> _get_speed(None, 15)
    (0.08, 15)

    >>> _get_speed(None, None)
    (0.08, 15)
    """
    seconds_per_dot = _seconds_per_dot(word_ref)
    if element_duration is None and wpm is None:
        #element_duration = 1
        #wpm = seconds_per_dot / element_duration
        wpm = WPM
        element_duration= wpm_to_duration(wpm, output='float', word_ref=WORD) / 1000.0
        return element_duration, wpm
    elif element_duration is not None and wpm is None:
        wpm = seconds_per_dot / element_duration
        return element_duration, wpm
    elif element_duration is None and wpm is not None:
        element_duration= wpm_to_duration(wpm, output='float', word_ref=WORD) / 1000.0
        return element_duration, wpm
    else:
        raise NotImplementedError("Can't set both element_duration and wpm")

def _numbers_units(N):
    """
    >>> _numbers_units(45)
    '123456789012345678901234567890123456789012345'
    """
    lst = range(1, N + 1)
    return "".join(list(map(lambda i: str(i % 10), lst)))

def _numbers_decades(N):
    """
    >>> _numbers_decades(45)
    '         1         2         3         4'
    """
    N = N // 10
    lst = range(1, N + 1)
    return "".join(map(lambda i: "%10s" % i, lst))

from enum import Enum
class ALIGN(Enum):
    """
    An Enum class for text alignement
    """
    LEFT = 0
    CENTER = 1
    RIGHT = 2

def _char_to_string_binary(c, align=ALIGN.LEFT, padding='-'):
    """
    >>> _char_to_string_binary('O', align=ALIGN.LEFT)
    'O----------'

    >>> _char_to_string_binary('O', align=ALIGN.RIGHT)
    '----------O'

    >>> _char_to_string_binary('O', align=ALIGN.CENTER)
    '-----O-----'
    """
    s_bin = mtalk.encode(c, encoding_type='binary', letter_sep=' ')
    N = len(s_bin)
    if align == ALIGN.LEFT:
        s_align = "<"
    elif align == ALIGN.RIGHT:
        s_align = ">"
    elif align == ALIGN.CENTER:
        s_align = "^"
    else:
        raise NotImplementedError("align '%s' not allowed" % align)
    s = "{0:" + padding + s_align + str(N) + "}"
    return s.format(c)

def _timing_representation(message):
    """
    Returns timing representation of a message like

             1         2         3         4         5         6         7         8
    12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789

    M------   O----------   R------   S----   E       C----------   O----------   D------   E
    ===.===...===.===.===...=.===.=...=.=.=...=.......===.=.===.=...===.===.===...===.=.=...=

    spoken reprentation:
    M   O   R   S  E          C    O   D  E
    -- --- .-. ... . (space) -.-. --- -.. .
    """
    s = _encode_to_binary_string(message, on="=", off=".")
    N = len(s)
    s += '\n' + _numbers_decades(N)
    s += '\n' + _numbers_units(N)
    s += '\n'
    s += '\n' + _timing_char(message)
    return s

def _timing_char(message):
    """
    >>> message = 'MORSE CODE'
    >>> _timing_char(message)
    'M------   O----------   R------   S----   E       C----------   O----------   D------   E'
    """
    s = ''
    inter_symb = ' '
    inter_char = ' ' * 3
    inter_word = inter_symb * 7
    for i, word in enumerate(_split_message(message)):
        if i >= 1:
            s += inter_word
        for j, c in enumerate(word):
            if j != 0:
                s += inter_char
            s += _char_to_string_binary(c, align=ALIGN.LEFT)
    return s

def _char_to_string_morse(c, align=ALIGN.CENTER, padding=' '):
    """
    >>> _char_to_string_morse('O')
    ' O '
    """
    bin = mtalk.encode(c, encoding_type='default', letter_sep=' ')
    N = len(bin)
    if align == ALIGN.LEFT:
        s_align = "<"
    elif align == ALIGN.RIGHT:
        s_align = ">"
    elif align == ALIGN.CENTER:
        s_align = "^"
    else:
        raise NotImplementedError("align '%s' not allowed" % align)
    s = "{0:" + padding + s_align + str(N) + "}"
    return s.format(c)

def _spoken_representation_L1(lst_lst_char):
    """
    >>> lst = [['M', 'O', 'R', 'S', 'E'], ['C', 'O', 'D', 'E']]
    >>> _spoken_representation_L1(lst)
    'M   O   R   S  E          C    O   D  E'

    >>> lst = [[], ['M', 'O', 'R', 'S', 'E'], ['C', 'O', 'D', 'E']]
    >>> _spoken_representation_L1(lst)
    '         M   O   R   S  E          C    O   D  E'
    """
    s = ''
    inter_char = ' '
    inter_word = inter_char * 9
    for i, word in enumerate(lst_lst_char):
        if i >= 1:
            s += inter_word
        for j, c in enumerate(word):
            if j != 0:
                s += inter_char
            s += _char_to_string_morse(c)
    return s

def _spoken_representation_L2(lst_lst_char):
    """
    >>> lst = [['M', 'O', 'R', 'S', 'E'], ['C', 'O', 'D', 'E']]
    >>> _spoken_representation_L2(lst)
    '-- --- .-. ... . (space) -.-. --- -.. .'
    """
    s = ''
    inter_char = ' '
    inter_word = ' (space) '
    for i, word in enumerate(lst_lst_char):
        if i >= 1:
            s += inter_word
        for j, c in enumerate(word):
            if j != 0:
                s += inter_char
            s += mtalk.encoding.morsetab[c]
    return s

def _spoken_representation(message):
    """
    Returns 2 lines of spoken representation of a message
    like:

             M   O   R   S  E          C    O   D  E
     (space) -- --- .-. ... . (space) -.-. --- -.. .
    """
    lst_lst_char = _split_message(message)
    s = _spoken_representation_L1(lst_lst_char)
    s += '\n' + _spoken_representation_L2(lst_lst_char)
    return s

def display(message, wpm, element_duration, word_ref, strip=False):
    """
    Display 
        text message
        morse code
        binary morse code
    """
    fmt = "{0:>8s}: '{1}'"
    key = "text"
    if strip:
        print(fmt.format(key, message.strip()))
    else:
        print(fmt.format(key, message.strip()))
    print(fmt.format("morse", mtalk.encode(message, strip=strip)))
    print(fmt.format("bin", mtalk.encode(message, encoding_type='binary', strip=strip)))
    print("")
    print("{0:>8s}:".format("timing"))
    print(_timing_representation(message))
    print("")
    print("{0:>8s}:".format("spoken reprentation"))
    print(_spoken_representation(message))
    print("")
    print("code speed : %s wpm" % wpm)
    print("element_duration : %s" % element_duration)
    print("reference word : %r" % word_ref)
    print("")

def _limit_value(value, upper=1.0, lower=0.0):
    """
    Returs value (such as amplitude) to upper and lower value
    
    >>> _limit_value(0.5)
    0.5

    >>> _limit_value(1.5)
    1.0

    >>> _limit_value(-1.5)
    0.0
    """
    if value > upper: return(upper)
    if value < lower: return(lower)
    return value

SECONDS_PER_DOT = _seconds_per_dot(WORD)  # 1.2

def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()