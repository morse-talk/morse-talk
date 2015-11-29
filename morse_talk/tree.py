#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Morse Binary Tree Implementation

Copyright (C) 2015 by
Sébastien Celles <s.celles@gmail.com>
All rights reserved.

CLI Usage
=========

$ python tree.py --c " ..."
{'-': {'-': {'char': '3'}, 'char': 'V'},
 '.': {'-': {'char': '4'}, '.': {'char': '5'}, 'char': 'H'},
 'char': 'S'}

$ python tree.py --c " ---"
{'-': {'-': {'char': '0'}, '.': {'char': '9'}},
 '.': {'.': {'.': {'char': ':'}, 'char': '8'}},
 'char': 'O'}

Dev usage
=========

mt = MorseBinaryTree()
print(mt['...'])

"""


import morse_talk as mtalk

class MorseBinaryTree(object):
    """
    Morse binary tree
    """

    def __init__(self, d=None, tree=None, char='char'):
        self._tree = {}

        self._char = char

        if d is None and tree is None:
            self._create_from_morse_dict(mtalk.encoding.morsetab)
        elif tree is not None:
            self._create_from_tree(tree)
        else:
            raise NotImplementedError("Can't create MorseBinaryTree")

    def _create_from_morse_dict(self, d_morse):
        for value, code in d_morse.items():
            if value != ' ':
                self._add(self._tree, value, code)

    def _create_from_tree(self, tree):
        self._tree = tree

    def _add(self, node, value, code):
        if code:
            self._add(node.setdefault(code[0], {}), value, code[1:])
        else:
            node[self._char] = value

    def __str__(self):
        return self._pretty_pprint()
        #return self._pretty_custom(self._tree)

    def _pretty_pprint(self):
        import pprint
        return pprint.pformat(self._tree)
    
    def _pretty_custom(self, d, indent_nb = 0, indent_char = '  '):
        s = ''
        for key, value in d.items():
            if key != self._char:
                s += (indent_char * indent_nb + str(key)) + '\n'
            if isinstance(value, dict):
                s += self._pretty_custom(value, indent_nb + 1)
            else:
                #s += ((indent_char * (indent_nb + 1) + str(value))) + '\n'
                s += "%20s\n" % value
            #s += '\n'
        return s

    @property
    def char(self):
        char = self._tree[self._char]
        return char

    @property
    def dit(self):
        return self['.']

    @property
    def dah(self):
        return self['-']

    def __getitem__(self, morse_code):
        if len(morse_code) == 1:
            tree = self._tree[morse_code]
            mt = MorseBinaryTree(tree=tree)
            return mt
        else:
            tree = self._tree[morse_code[0]]
            mt = MorseBinaryTree(tree=tree)[morse_code[1:]]
            return mt

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Display morse binary tree')
    parser.add_argument('--c', help='Morse code character', default='')
    args = parser.parse_args()
    c = args.c.strip()

    mt = MorseBinaryTree()
    if c == '':
        print(mt)
    else:
        print(mt[c])

if __name__ == '__main__':
    main()
