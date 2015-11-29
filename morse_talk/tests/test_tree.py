#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equals
import morse_talk as mtalk
from morse_talk.tree import MorseBinaryTree

mt = mtalk.tree.MorseBinaryTree()

def test_tree_pretty():
    print(mt)
    # printing tree shouldn't raises exception

def test_tree_getitem_len1():
    assert_equals(mt['.'].char, 'E')
    assert_equals(mt['-'].char, 'T')
    assert_equals(mt['.']['.']['.'].char, 'S')
    assert_equals(mt['-']['-']['-'].char, 'O')

def test_tree_properties_dit_dah():
    assert_equals(mt.dit.dit.dit.char, 'S')
    assert_equals(mt.dah.dah.dah.char, 'O')

def test_tree_getitem_len3():
    assert_equals(mt['...'].char, 'S')
    assert_equals(mt['---'].char, 'O')
