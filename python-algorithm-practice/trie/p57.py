"""
    Problem 57: Palindrome Pairs

    Question: Find all index combinations (i, j) in a list of words where words[i] + words[j] are palindromic
    Source: leetcode 336 (https://leetcode.com/problems/palindrome-pairs/

"""
import collections
from typing import List
from common.common_function import test_result


# Solution 1: Using brute force
def palindrome_pairs_1(words: List[List[str]]) -> List[List[int]]:
    def is_palindrome(word):
        return word == word[::-1]

    output = []
    for i, word_1 in enumerate(words):
        for j, word_2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word_1 + word_2):
                output.append([i, j])

    return output


# Solution 2: Using trie
class TrieNode2:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode2)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie2:
    def __init__(self):
        self.root = TrieNode2()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def index(self, index: int, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index: int, word: str) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


def palindrome_pairs_2(words: List[str]) -> List[List[int]]:
    trie = Trie2()

    for i, word in enumerate(words):
        trie.index(i, word)

    results = []
    for i, word in enumerate(words):
        results.extend(trie.search(i, word))

    return results


function_list = [palindrome_pairs_1, palindrome_pairs_2]


if __name__ == "__main__":
    list_len = len(function_list)
    str_list_1 = ["abcd", "dcba", "lls", "s", "sssll"]
    test_result("Word list", function_list, str_list_1)
    print()
    str_list_2 = ["bat", "tab", "cat"]
    test_result("Word list", function_list, str_list_2)
