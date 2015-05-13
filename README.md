# morse-talk
morse-talk is a morse aide written in python.

## Usage
```python
>>> import morse_talk as mtalk

>>> mtalk.encode('Alpha Ranger 45 departed')
'.-   .-..   .--.   ....   .-       .-.   .-   -.   --.   .   .-.       ....-   .....
       -..   .   .--.   .-   .-.   -   .   -..'

>>> mtalk.encode('Alpha Ranger 45 knocked down', encoding='binary')
'1111000111111000111111110001111000111100000001111100011110001111000111111100010001111
10000000111111100011111000000011111110001111000111111111000111111110001111111000100011
11100000001111100011111111100011111110001111'

>>> code = '-...   ---   --   -...       -..-       .--.   --'
>>> mtalk.decode(code)
'bomb x pm'
```