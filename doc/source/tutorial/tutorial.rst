..  -*- coding: utf-8 -*-

.. currentmodule:: morse_talk

Start here to begin working with Morse Talk.


Encode a message
----------------

Create a message you want to encode.

>>> import morse_talk as mtalk
>>> message = "Hi, I'll be there by 10 PM"


``message`` is a Python string. No leading or trailing
whitespaces are allowed in it. Even if it is there, it
will be truncated off for encoding.

Now encode your message in Morse Code.

>>> code = mtalk.encode(message)
>>> code
'....   ..   --..--       ..   .----.   .-..   .-..       -...   .       -   ....   .   .-.   .       -...   -.--       .----   -----       .--.   --'

.. Note::
	Morse Talk supports alphabets, numerals and some special 
	characters only. If any unsupported character is present
	in the ``message``, it will be ignored.

	>>> message = "Congratualtion!"
	>>> mtalk.encode(message)
	WARNING: Unsupported characters in the string
	'-.-.   ---   -.   --.   .-.   .-   -   ..-   .-..   .-   -   ..   ---   -.   ...'

You can also encode the message in binary encoding style.

>>> mtalk.encode(code, 'binary')


Decode a message
----------------

Decode the message which you have encoded in Morse Code.

>>> code = '.-   .-..   .--.   ....   .-       ....-   .....       -..   .   .--.   .-   .-.   -   .   -..'
>>> message = mtalk.decode(code)
>>> message
'alpha 45 departed'

>>> code = '101010001110111011100010101'
>>> mtalk.decode(code, 'binary')
'SOS'
