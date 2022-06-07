"""
    Problem 21: Remove Duplicate Letters

    Question: Remove duplicate letters and sort by lexicographical order
    Source: leetcode 316 (https://leetcode.com/problems/remove-duplicate-letters/
"""
import collections

from common.common_function import test_result


# Solution 1: Using recursion
def remove_duplicate_letters_1(s: str) -> str:
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + remove_duplicate_letters_1(suffix.replace(char, ''))
    return ''


# Solution 2: Using stack
def remove_duplicate_letters_2(s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)


function_list = [remove_duplicate_letters_1, remove_duplicate_letters_2]


if __name__ == "__main__":
    input_1 = 'bcabc'
    test_result('String', function_list, input_1)
    print()
    input_2 = 'cbacdcbc'
    test_result('String', function_list, input_2)
