"""
    Problem 2. Valid Palindrome

    Question: Make function that reverts given String array
    Source: leetcode 344 (https://leetcode.com/problems/reverse-string/

"""

# Solution 1: Using two pointer
import time
from typing import List


def reverse_string_1(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Solution 1: Pythonic way
def reverse_string_2(s: List[str]) -> None:
    s.reverse()  # s[:] = s[::-1]


def test_result(list_input: List[str]):
    print(f'Input -> {list_input}')

    result_list_1 = list_input[:]
    result_list_2 = list_input[:]

    start_1 = time.perf_counter()
    reverse_string_1(result_list_1)
    end_1 = time.perf_counter()
    time_elapsed_1 = end_1 - start_1

    print(f'Solution 1 Result: {result_list_1}')
    print(f'Solution 1 Time elapsed: {time_elapsed_1}')

    start_2 = time.perf_counter()
    reverse_string_2(result_list_2)
    end_2 = time.perf_counter()
    time_elapsed_2 = end_2 - start_2

    print(f'Solution 2 Result: {result_list_2}')
    print(f'Solution 2 Time elapsed: {time_elapsed_2}')

    if time_elapsed_1 < time_elapsed_2:
        print("Solution 1 was the fastest!")
    else:
        print("Solution 2 was the fastest!")


if __name__ == "__main__":
    list_input_1 = ['h', 'e', 'l', 'l', 'o']
    test_result(list_input_1)
    print()
    list_input_2 = ['H', 'a', 'n', 'n', 'a', 'h']
    test_result(list_input_2)

