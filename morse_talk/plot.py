#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Morse Binary plot

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.
"""

import matplotlib.pyplot as plt
import morse_talk as mtalk

def _create_ax(ax):
    """
    Create a Matplotlib Axe from ax
    if ax is None a new Matplotlib figure is create
        and also an ax
    else ax is returned
    """
    if ax is None:
        fig, axs = plt.subplots(1, 1)
        return axs
    else:
        return ax

def _create_x_y(l, duration=1):
    """
    Create 2 lists
        x: time (as unit of dot (dit)
        y: bits
    from a list of bit

    >>> l = [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1]
    >>> x, y = _create_x_y(l)
    >>> x
    [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27, 28]
    >>> y
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
    """
    l = [0] + l + [0]
    y = []
    x = []
    for i, bit in enumerate(l):
        y.append(bit)
        y.append(bit)
        x.append((i - 1) * duration)
        x.append(i * duration)
    return x, y

def plot(message, duration=1, ax = None):
    """
    Plot a message

    Returns: ax a Matplotlib Axe
    """
    lst_bin = mtalk.encoding._encode_binary(message)
    x, y = _create_x_y(lst_bin, duration)
    ax = _create_ax(ax)
    ax.plot(x, y, linewidth=2.0)
    delta_y = 0.1
    ax.set_ylim(-delta_y, 1 + delta_y)
    ax.set_yticks([0, 1])
    delta_x = 0.5 * duration
    ax.set_xlim(-delta_x, len(lst_bin) * duration + delta_x)
    return ax

def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()
