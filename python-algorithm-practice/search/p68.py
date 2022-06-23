"""
    Problem 68: Two Sum II - Input array is sorted

    Question: Return the two numeric indices of the array that can be added to form the target be given sorted array
    * Index starts from 1 instead of 0
    Source: leetcode 349 (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
import bisect
from typing import Any, List
from common.common_function import test_result_single


# Solution 1: Using two pointers
def two_sum_1(numbers: List[int], target: int) -> Any:
    left, right = 0, len(numbers) - 1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left + 1, right + 1


# Solution 2: Using binary search
def two_sum_2(numbers: List[int], target: int) -> Any:
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        expected = target - v
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                return k + 1, mid + 1


# Solution 3: Using bisect module + slicing
def two_sum_3(numbers: List[int], target: int) -> Any:
    for k, v in enumerate(numbers):
        expected = target - v
        i = bisect.bisect_left(numbers[k + 1:], expected)
        if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
            return k + 1, i + k + 2


# Solution 4: Using bisect module + slicing minimum
def two_sum_4(numbers: List[int], target: int) -> Any:
    for k, v in enumerate(numbers):
        expected = target - v
        nums = numbers[k + 1:]
        i = bisect.bisect_left(nums, expected)
        if i < len(numbers[k + 1:]) and numbers[i + k + 1] == expected:
            return k + 1, i + k + 2


# Solution 5: Using bisect module + slicing deleting
def two_sum_5(numbers: List[int], target: int) -> Any:
    for k, v in enumerate(numbers):
        expected = target - v
        nums = numbers[k + 1:]
        i = bisect.bisect_left(nums, expected, k + 1)
        if i < len(numbers) and numbers[i] == expected:
            return k + 1, i + k + 2


function_list = [two_sum_1, two_sum_2, two_sum_3, two_sum_4, two_sum_5]


if __name__ == "__main__":
    lg = len(function_list)
    number_list = [2, 7, 11, 15]
    target_num = 9
    print(f"Given Input Info: numbers = {number_list}, target = {target_num}", end='\n\n')
    result_lists = [test_result_single(i, function_list, number_list, target_num) for i in range(lg)]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
