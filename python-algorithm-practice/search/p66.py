"""
    Problem 66: Search in Rotated Sorted Array

    Question: Print the index of the target value in a sorted array rotated around a specific pivot.
    * The distance between two points on a plane is the Euclidean distance.
    Source: leetcode 33 (https://leetcode.com/problems/search-in-ratated-sorted-array/

"""
import heapq
from typing import Any, List
from common.common_function import test_result_single


# Solution: Using binary search using pivot
def search_pivot(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1


function_list = [search_pivot]


if __name__ == "__main__":
    num_list = [4, 5, 6, 7, 0, 1, 2]
    num_target = 1
    print(f"Given Input Info: nums = {num_list}, target = {num_target}", end='\n\n')
    test_result_single(0, function_list, num_list, num_target)
