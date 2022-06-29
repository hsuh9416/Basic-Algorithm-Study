"""
    Problem 86: Maximum Subarray

    Question: Return the subarray of which is the maximum sum
    Source: leetcode 53 (https://leetcode.com/problems/maximum-subarray/
"""
import sys
from typing import List

from common.common_function import test_result


# Solution 1: Using memoization
def max_subarray_1(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
    return max(nums)


# Solution 2: Using Kadane's algorithm
def max_subarray_2(nums: List[int]) -> int:
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


function_list = [max_subarray_1, max_subarray_2]


if __name__ == "__main__":
    num_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test_result('Number List', function_list, num_list)
