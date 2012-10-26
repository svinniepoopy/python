#!/usr/bin/env python
""" main.py

@author Akhil Jaggarwal
@created Tue Oct 23 15:45:29 EDT 2012

main file for reading words and building 
the word dictionary.

STATUS: currently using difflib for best matches and vowels 
       are only corrected upto one character, working on 
       improving that, also working on the extra credit section
"""

import sys
import string
from SpellCheck import *
from SpellTrie import *

tree = SpellTrie()

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

def process(word):
    """ get a word from console and try to spell check """
    SC = SpellCheck(word)
    try:
        if SC.getWord(tree) is not None:
            return SC.getWord(tree)
    except TypeError:
        return 'NO SUGGESTION'

if __name__ == '__main__':
    """ read from default /usr/share/dict/english.dict """
    print '--- begin spellcheck ---'
    tree = buildTrie() 

    while True:
        print '> ',
        in_word = ''
        try:
            word = raw_input(in_word)
            print process(word)
        except (ValueError, EOFError, KeyboardInterrupt):
            sys.exit() # be silent
