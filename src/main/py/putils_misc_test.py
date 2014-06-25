from putils_misc import RankedTrie
from putils_misc import ImageManipulator
import glob
import shutil
import os

import unittest

class TestRankedTrie(unittest.TestCase):

    def test_autocomplete_with_ranking(self):
        trie = RankedTrie()
        trie.insert("hello", 1)
        trie.insert("hemophiliac", 3)
        trie.insert("apple", 33)
        trie.insert("apple pie", 22)
        trie.insert("apple tart", 21)
        trie.insert("aardvark", 444)

        p = trie.autocomplete_with_rank("a", 2)
        self.assertTrue(len(p)==2)
        p = trie.autocomplete_with_rank("a")
        self.assertTrue(len(p)==4)
        p = trie.autocomplete_with_rank("he")
        self.assertTrue(len(p)==2)
        self.assertTrue(p[0][0]=="hemophiliac")

if __name__ == '__main__':
    """
    Needed to run unittests in CLI or PyCharm
    """
    unittest.main()
