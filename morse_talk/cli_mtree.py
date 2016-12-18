#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Morse Binary CLI tool to deals with morse code tree

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.

Usage:
$ mtree -c " .-"
"""

import argparse

from morse_talk.tree import MorseBinaryTree


def main():
    parser = argparse.ArgumentParser(description='Display morse binary tree')
    parser.add_argument('-c', '--c', help='Morse code character', default='')
    args = parser.parse_args()
    c = args.c.strip()

    mt = MorseBinaryTree()
    print(mt[c])

if __name__ == '__main__':
    main()
