# morse-talk
morse-talk is a morse aide written in python.

## Usage
```python
>>> import morse_talk as mtalk

>>> mtalk.encode('Alpha Ranger 45 departed')
'.-   .-..   .--.   ....   .-       .-.   .-   -.   --.   .   .-.       ....-   .....       -..   .   .--.   .-   .-.   -   .   -..'

>>> mtalk.encode('Alpha Ranger 45 knocked down', encoding='binary')
'11110001111110001111111100011110001111000000011111000111100011110001111111000100011111000000011111110001111100000001111111000111100011111111100011111111000111111100010001111100000001111100011111111100011111110001111'