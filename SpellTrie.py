"""
SpellTrie.py

@author: [CITE]: github.com/bdimmick/python-trie

find words with differ in single or more 
characters. Used (an implementation) of trie for 1) faster O(len(word))
lookups and 2) prefix matching. Could also be done by just using a vector
and a DFS by generating all possible outcomes for an input word, perhaps
more of a C/C++ solution than Python.
"""

class SpellTrie:

    def __init__(self):
        self.path = {}
        self.value = None
        self.value_valid = False

    def __setitem__(self, key, value):
        """ set a key, value pair recursively in the trie, pretty slow """
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = SpellTrie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.__setitem__(remains, value)
        else:
            node.value = value
            node.value_valid = True           

    def __getitem__(self, key):
        """ get a key, value, pair from the trie """
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            raise KeyError(key)
        if len(key) > 1:
            remains = key[1:]
            try:
                return node.__getitem__(remains)
            except KeyError:
                raise KeyError(key)
        elif node.value_valid:
            return node.value
        else:
            raise KeyError(key)

    def hasKey(self, key):
        """ boolean accessor """
        try:
            self.__getitem__(key)
        except KeyError:
            return False
        return True

    def getKey(self, key, default=None):
        """ accessor for a key """
        try:
            return self.__getitem__(key)
        except KeyError:
            return default, "key not present"

    def keys(self, prefix=[]):
        """ override default keys() """
        result = []
        if self.value_valid:
            isStr = True
            val = ""
            for k in prefix:
                if type(k) != str or len(k) > 2:
                    isStr = False
                    break
                else:
                    val += k
            if isStr:
                result.append(val)
            else:
                result.append(prefix)
        for k in self.path.iterkeys():
            next = []
            next.extend(prefix)
            next.append(k)
            result.extend(self.path[k].keys(next))
        return result
