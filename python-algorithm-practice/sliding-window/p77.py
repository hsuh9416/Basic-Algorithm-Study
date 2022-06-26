"""
    Problem 77: Longest Repeating Character Replacement

    Question: Given a string of uppercase letters s, print the longest length of a consecutively repeated string that can be made with k changes
    Source: leetcode 424 (https://leetcode.com/problems/longest-repeating-character-replacement/
"""
import collections
from common.common_function import test_result_2


# Solution: Using two pointer, sliding window, counter
def character_replacement(s: str, k: int) -> int:
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1
        max_char_n = counts.most_common(1)[0][1]

        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1

    return right - left


function_list = [character_replacement]


if __name__ == "__main__":
    str_s = 'AAABBC'
    int_k = 2
    test_result_2('Strings', function_list, str_s, int_k)
