"""
SpellCheck.py

@author Akhil Jaggarwal
@created Wed Oct 24 12:19:04 EDT 2012

prints best spelling suggestion based rules or nothing.

scrubs input words for case, repeated letters and incorrect vowel errors.
"""
import string
import difflib
from SpellTrie import *

class SpellCheck():

    VOWELS = ['a','e','i','o','u']
    def __init__(self, word):
	self.word = word

    def __scrubWord__(self):
	return self.word.strip()
    
    def __correctCase__(self):
	return self.word.lower()

    def __removeDuplicates__(self, word, tree):
	""" use difflib for sequence matching
	    returns list of closest matches
	"""
	d = difflib
	try:
	    key = d.get_close_matches(word, tree.keys(), 1)[0]
	    return key
	except IndexError:
	    return None

    def __correctVowels__(self, word, tree):
	word = self.word
	""" return word if valid """
	if tree.hasKey(word):
	    return tree.getKey(word)
	""" else change every vowel in word from VOWELS """
	for char_index, ch in list(enumerate(word[:])):
	    if ch in self.VOWELS[char_index]:
		for vowel in self.VOWELS:
		    new_word = string.replace(word, ch, vowel, 1)
		    self.word = new_word
		    if tree.hasKey(self.word):
			return tree.getKey(self.word)
		    else:
			continue
	    else:
		continue
	return None

    def getWord(self, tree):	   
	word = self.word
	""" scrub to remove extra spaces/tabs """
	word  = self.__scrubWord__()
	""" correct case regardless to minimize errors """
	word = self.__correctCase__()
	""" remove duplicates, if any """
	key = self.__removeDuplicates__(word, tree)
	""" loop through, till a valid key is found
	    consider cases:
	    1) key already exist 
	    2) duplicates need to be removed
	    3) vowels need to be fixed
	"""
	while True:
	    try:
		if tree.hasKey(word):
		    return tree.getKey(word)	    
		    break
		elif tree.hasKey(self.__correctVowels__(word, tree)):
		    try:
			return tree.hasKey(self.__correctVowels__(word, tree))
		    except IndexError:
			continue
		elif tree.hasKey(key):
		    return tree.getKey(key)
		    break
		else:
		    return None
		    break
	    except (KeyError, TypeError):
		return None
	    	break
