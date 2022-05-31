"""
    Problem 5. Group Anagrams

    Question: Grouping by anagram from given String array
    Source: leetcode 49 (https://leetcode.com/problems/group-anagrams/

"""
import collections
from typing import List
import time


# Solution: Sort then add to Dictionary
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


def test_result(strs: List[str]) -> None:
    start_1 = time.perf_counter()
    result = group_anagrams(strs)
    end_1 = time.perf_counter()
    time_elapsed_1 = end_1 - start_1

    print(f'Solution Result: {result}')
    print(f'Solution Time elapsed: {time_elapsed_1}')


if __name__ == "__main__":
    str_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    test_result(str_list)
