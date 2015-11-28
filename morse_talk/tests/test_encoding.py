#!/usr/bin/env python
from nose.tools import *
import morse_talk as mtalk

class TestEncoding:

    def test_encoding_default(self):
        message = 'This is a test for default encoding.'
        message = message.upper()
        morse_code = mtalk.encode(message)
        morse_code_expected = ('-   ....   ..   ...       ..   ...       .-       -   .'
            '   ...   -       ..-.   ---   .-.       -..   .   ..-.   .-   ..- '
            '  .-..   -       .   -.   -.-.   ---   -..   ..   -.   --.   .-.-.-'
            )
        assert_equal(morse_code, morse_code_expected)

    def test_encoding_binary(self):
        message = 'This is a test for binary encoding.'
        message = message.upper()
        morse_code = mtalk.encode(message)
        morse_code_expected = ('-   ....   ..   ...       ..   ...       .-       -   .'
            '   ...   -       ..-.   ---   .-.       -...   ..   -.   .-   .-.'
            '   -.--       .   -.   -.-.   ---   -..   ..   -.   --.   .-.-.-'
            )
        assert_equal(morse_code, morse_code_expected)


    def test_encode_morse1(self):
        message = 'MORSE CODE'
        morse_code = mtalk.encode(message)
        morse_code_expected = "--   ---   .-.   ...   .       -.-.   ---   -..   ."
        assert_equal(morse_code, morse_code_expected)

    def test_encode_morse2(self):
        message = 'Alpha Ranger 45 departed'
        morse_code = mtalk.encode(message)
        morse_code_expected = (".-   .-..   .--.   ....   .-       "
                ".-.   .-   -.   --.   .   .-.       ....-   .....       -..   .   .--.   .-   .-.   -   .   -..")
        assert_equal(morse_code, morse_code_expected)

    def test_encode_binary(self):
        message = 'Alpha Ranger 45 knocked down'
        binary = mtalk.encode(message, encoding_type='binary')
        binary_expected = ('10111000101110101000101110111010001010101000101110000000'
            '10111010001011100011101000111011101000100010111010000000'
            '10101010111000101010101000000011101011100011101000111011'
            '10111000111010111010001110101110001000111010100000001110'
            '1010001110111011100010111011100011101')
        assert_equal(binary, binary_expected)

    def test_encode_binary2(self):
        message = 'MORSE CODE'
        binary = mtalk.encode(message, encoding_type='binary')
        binary_expected = ('11101110001110111011100010111010001010100010000000'
            '111010111010001110111011100011101010001')
        assert_equal(binary, binary_expected)

class TestDecoding:

    def test_decoding_default(self):
        code = ('-   ....   ..   ...       ..   ...       .-       -   .'
            '   ...   -       ..-.   ---   .-.       -..   .   ..-.   .-   ..- '
            '  .-..   -       .   -.   -.-.   ---   -..   ..   -.   --.   .-.-.-'
            )
        message = mtalk.decode(code)
        message_expected = 'THIS IS A TEST FOR DEFAULT ENCODING.'
        assert_equal(message, message_expected)

    def test_decode_morse(self):
        morse = '-...   ---   --   -...       -..-       .--.   --'
        message = mtalk.decode(morse)
        message_expected = 'BOMB X PM'
        assert_equal(message, message_expected)

    def test_decode_binary(self):
        message = 'MORSE CODE'
        binary = mtalk.encode(message, encoding_type='binary')
        message_decoded = mtalk.decode(binary, encoding_type='binary')
        assert_equal(message_decoded, message)
