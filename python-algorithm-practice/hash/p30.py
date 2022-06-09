"""
    Problem 30: Longest Substring Without Repeating Characters

    Question: Return the length of the longest substring without repeating characters from given string
    Source: leetcode 3 (https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
from common.common_function import test_result


# Solution : Using sliding window and two pointer
def length_of_longest_substring(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index

    return max_length


function_list = [length_of_longest_substring]


if __name__ == "__main__":
    string_1 = "abcabcbb"
    test_result('String', function_list, string_1)
    print()
    string_2 = "bbbbb"
    test_result('String', function_list, string_2)
    print()
    string_3 = "pwwkew"
    test_result('String', function_list, string_3)
