"""
    Problem 69: Single Number

    Question: All but one element have two. Find one element.
    Source: leetcode 136 (https://leetcode.com/problems/single-number/
"""
from typing import List
from common.common_function import test_result_single


# Solution: Solving XOR
def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num

    return result


function_list = [single_number]


if __name__ == "__main__":
    number_list_1 = [2, 2, 1]
    print(f"Given Input Info: numbers = {number_list_1}", end='\n\n')
    test_result_single(0, function_list, number_list_1)
    print()
    number_list_2 = [4, 1, 2, 1, 2]
    print(f"Given Input Info: numbers = {number_list_2}", end='\n\n')
    test_result_single(0, function_list, number_list_2)
