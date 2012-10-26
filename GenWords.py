#!/usr/bin/env python
""" main.py

@author Akhil Jaggarwal
@created Wed Oct 24 23:08:21 EDT 2012

extra credit: generate words containing the three
class of spelling errors.
"""

import sys
import string
import random
from SpellTrie import *

VOWELS = ['a','e','i','o','u']

tree = SpellTrie()

def genWords(word):
    """ return a list of words with spelling mistakes
        GENERATE: case errors, repeated letters and
        incorrect vowels
    """
    err_word_list_vowel = []
    err_word_list = []
    # vowels
    for char_index, ch in list(enumerate(word[:])):
        if ch in VOWELS:
            for vowel in VOWELS:
                if ch != vowel:
                    err_word = string.replace(word, ch, vowel, 1)
                    rand_int = random.randint(0,len(err_word)-1)
                    # case
                    err_word_case = string.replace(err_word, \
                            err_word[rand_int], \
                            err_word[rand_int].upper(),1)
                    if not tree.hasKey(err_word):
                        err_word_list.append(err_word_case)
                        err_word_list_vowel.append(err_word_case)

    # character repetitions    
    for word in err_word_list_vowel:
        len_w = len(word)
        rand_int = random.randint(0, len_w-1)
        # do a simple random character repetition
        for i in range(0,rand_int):
            err_word_rep = string.replace(word, \
                    word[rand_int],
                    word[rand_int]*i,1)
            err_word_list.append(err_word_rep)
    
    return err_word_list

def buildTrie():
    """Read in the list of words from /usr/share/dict
       and return a tree
    """
    source = '/usr/share/dict/english.dict'
    word_file = open(source, 'r+')
    data = word_file.readlines()
    for k, v in enumerate(data):
        """ had to add rstrip() to remove trailing characters """
        vlowercase = v.lower().rstrip()
        tree[vlowercase] = vlowercase
    return tree
 
def process(in_word):
    """ get a word from console and try to generate words 
        with spelling mistakes
    """
    word = in_word.lower().rstrip()
    return genWords(word)

if __name__ == '__main__':
    buildTrie()
    in_word = ''
    try:
        print '> ',
        word = raw_input(in_word)
        print process(word)
    except EOFError:
        sys.exit() # be silent
