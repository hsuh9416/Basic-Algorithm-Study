"""
    Problem 83: Majority Element

    Question: Print the majority element
    Source: leetcode 169 (https://leetcode.com/problems/majority-element/
"""
import collections
from typing import Any, List
from common.common_function import test_result


# Solution 1: Using brute force
def majority_element_1(nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num


# Solution 2: Using dynamic programing
def majority_element_2(nums: List[int]) -> int:
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            return num


# Solution 3: Using divide and conquer
def majority_element_3(nums: List[int]) -> Any:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = majority_element_3(nums[:half])
    b = majority_element_3(nums[half:])

    return [b, a][nums.count(a) > half]


# Solution 4: Using divide and conquer
def majority_element_4(nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]


function_list = [majority_element_1, majority_element_2, majority_element_3, majority_element_4]


if __name__ == "__main__":
    num_list_1 = [3, 2, 3]
    test_result('Number List', function_list, num_list_1)
    print()
    num_list_2 = [2, 2, 1, 1, 1, 2, 2]
    test_result('Number List', function_list, num_list_2)
