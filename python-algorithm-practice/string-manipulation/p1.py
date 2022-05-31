"""
    Problem 1. Valid Palindrome

    Question: Find out if the given String is a palindrome(A word that remains the same after reversion)
    Source: leetcode 125 (https://leetcode.com/problems/valid-palindrome/

"""
import collections
from typing import Deque
import re
import time

input1 = "A man, a plan, a canal: Panama"
input2 = "race a car"


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
    s = re.sub('[^a-z0-9]','', s)
    return s == s[::-1]


def test_result1():
    start = time.perf_counter()
    print(input1, '->', is_palindrome_1(input1))
    end = time.perf_counter()
    print('test 1 time elapsed:', end='')
    print(end-start)
    start = time.perf_counter()
    print(input2, '->', is_palindrome_1(input2))
    end = time.perf_counter()
    print('test 2 time elapsed:', end='')
    print(end-start)



def test_result2():
    start = time.perf_counter()
    print(input1, '->', is_palindrome_2(input1))
    end = time.perf_counter()
    print('test 1 time elapsed:', end='')
    print(end-start)
    start = time.perf_counter()
    print(input2, '->', is_palindrome_2(input2))
    end = time.perf_counter()
    print('test 2 time elapsed:', end='')
    print(end-start)


def test_result3():
    start = time.perf_counter()
    print(input1, '->', is_palindrome_3(input1))
    end = time.perf_counter()
    print('test 1 time elapsed:', end='')
    print(end-start)
    start = time.perf_counter()
    print(input2, '->', is_palindrome_3(input2))
    end = time.perf_counter()
    print('test 2 time elapsed:', end='')
    print(end-start)


if __name__ == "__main__":
    test_result1()
    test_result2()
    test_result3()

