"""
    Problem 67: Intersection of Two Arrays

    Question: Find the intersection of two arrays
    Source: leetcode 349 (https://leetcode.com/problems/intersection-of-two-arrays/

"""
import bisect
from typing import Any, List
from common.common_function import test_result_single


# Solution 1: Using brute force
def intersection_1(nums1: List[int], nums2: List[int]) -> Any:
    result = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return result


# Solution 2: Using binary search
def intersection_2(nums1: List[int], nums2: List[int]) -> Any:
    result = set()
    nums2.sort()
    for n1 in nums1:
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return result


# Solution 3: Using two pointers
def intersection_3(nums1: List[int], nums2: List[int]) -> Any:
    result = set()
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return result


function_list = [intersection_1, intersection_2, intersection_3]


if __name__ == "__main__":
    lg = len(function_list)
    num1_lists_1 = [[1, 2, 2, 1] for i in range(len(function_list))]
    num2_lists_1 = [[2, 2] for i in range(len(function_list))]
    print(f"Given Input Info: nums1 = {num1_lists_1[0]}, nums2 = {num2_lists_1[0]}", end='\n\n')
    result_lists = [test_result_single(i, function_list, num1_lists_1[i], num2_lists_1[i]) for i in range(lg)]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
    print()
    num1_lists_2 = [[4, 9, 5] for i in range(len(function_list))]
    num2_lists_2 = [[9, 4, 9, 8, 4] for i in range(len(function_list))]
    print(f"Given Input Info: nums1 = {num1_lists_2[0]}, nums2 = {num2_lists_2[0]}", end='\n\n')
    result_lists = [test_result_single(i, function_list, num1_lists_2[i], num2_lists_2[i]) for i in range(lg)]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
