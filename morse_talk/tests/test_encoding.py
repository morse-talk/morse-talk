#!/usr/bin/env python
from nose.tools import *
import morse_talk as mtalk

class TestEncoding:

	def test_encoding_defualt(self):
		code = mtalk.encode('This is a test for default encoding.')
		morse_code = ('-   ....   ..   ...       ..   ...       .-       -   .'
			'   ...   -       ..-.   ---   .-.       -..   .   ..-.   .-   ..- '
			'  .-..   -       .   -.   -.-.   ---   -..   ..   -.   --.   .-.-.-'
			)
		assert_equal(code, morse_code)

	def test_encoding_binary(self):
		code = mtalk.encode('This is a test for binary encoding.')
		morse_code = ('-   ....   ..   ...       ..   ...       .-       -   .'
			'   ...   -       ..-.   ---   .-.       -...   ..   -.   .-   .-.'
			'   -.--       .   -.   -.-.   ---   -..   ..   -.   --.   .-.-.-'
			)
		assert_equal(code, morse_code)

class TestDecoding:

	def test_decoding_default(self):
		code = ('-   ....   ..   ...       ..   ...       .-       -   .'
			'   ...   -       ..-.   ---   .-.       -..   .   ..-.   .-   ..- '
			'  .-..   -       .   -.   -.-.   ---   -..   ..   -.   --.   .-.-.-'
			)
		message = mtalk.decode(code)
		assert_equal(message, 'this is a test for default encoding.')