"""
    Problem 65: Binary Search

    Question: Find the index matches with the given value, using binary search with sorted given list nums
    Source: leetcode 704 (https://leetcode.com/problems/binary-search/

"""
import bisect
from typing import List
from common.common_function import test_result_single


# Solution 1: Using recursive structure
def binary_search_1(nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1

    return binary_search(0, len(nums) - 1)


# Solution 2: Using repetitive structure
def binary_search_2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


# Solution 3: Using binary search module
def binary_search_3(nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1


# Solution 4: Using index but not binary search module
def binary_search_4(nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1


function_list = [binary_search_1, binary_search_2, binary_search_3, binary_search_4]


if __name__ == "__main__":
    num_list = [-1, 0, 3, 5, 9, 12]
    num_target = 9
    print(f"Given Input Info: nums = {num_list}, target = {num_target}", end='\n\n')
    result_lists = [test_result_single(i, function_list, num_list, num_target) for i in range(len(function_list))]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
