"""
    Problem 56: Implement trie (Prefix Tree)

    Question: Implement the following methods in Trie
    * Trie methods
        insert(), search(), startWith()

    Source: leetcode 208 (https://leetcode.com/problems/implement-trie-prefix-tree/

"""
import collections
from common.common_function import test_function


# Solution: Using dictionary
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


if __name__ == "__main__":
    trie = Trie()
    test_function('insert', trie.insert, "apple")
    test_function('search', trie.search, "apple")
    test_function('search', trie.search, "app")
    test_function('startWith', trie.starts_with, "app")
    test_function('insert', trie.insert, "app")
    test_function('search', trie.search, "app")
