"""
    Problem 1. Valid Palindrome

    Question: Find out if the given String is a palindrome(A word that remains the same after reversion)
    Source: leetcode 125 (https://leetcode.com/problems/valid-palindrome/

"""
import collections
from typing import Deque
import re
import time


# Solution 1: Convert as list
def is_palindrome_1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


# Solution 2: Using Deque -> Faster than Solution 1, because popleft is O(1) while pop(0) is O(n)
def is_palindrome_2(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# Solution 3: Using slicing -> Even faster than Solution 2, because this solution merged looping of isalnum
# Slicing is internally implemented in C and efficient than standard while looping -> Because of pointer manipulation
def is_palindrome_3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


def test_result(text_input):
    print(f'Input -> {text_input}')

    start_1 = time.perf_counter()
    result_1 = is_palindrome_1(text_input)
    end_1 = time.perf_counter()
    time_elapsed_1 = end_1 - start_1

    print(f'Solution 1 Result: {result_1}')
    print(f'Solution 1 Time elapsed: {time_elapsed_1}')

    start_2 = time.perf_counter()
    result_2 = is_palindrome_2(text_input)
    end_2 = time.perf_counter()
    time_elapsed_2 = end_2 - start_2

    print(f'Solution 2 Result: {result_2}')
    print(f'Solution 2 Time elapsed: {time_elapsed_2}')

    start_3 = time.perf_counter()
    result_3 = is_palindrome_3(text_input)
    end_3 = time.perf_counter()
    time_elapsed_3 = end_3 - start_3

    print(f'Solution 3 Result: {result_3}')
    print(f'Solution 3 Time elapsed: {time_elapsed_3}')

    result = min(time_elapsed_1, time_elapsed_2, time_elapsed_3)
    if result == time_elapsed_1:
        print("Solution 1 was the fastest!")
    elif result == time_elapsed_2:
        print("Solution 2 was the fastest!")
    else:
        print("Solution 3 was the fastest!")


if __name__ == "__main__":
    input1 = "A man, a plan, a canal: Panama"
    test_result(input1)
    print()
    input2 = "race a car"
    test_result(input2)
