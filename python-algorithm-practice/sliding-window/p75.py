"""
    Problem 75: Sliding Window Maximum

    Question: Given an array of nums, find the maximum sliding window by moving a sliding window of size k all the way to the right
    Source: leetcode 239 (https://leetcode.com/problems/sliding-window-maximum/
"""
import collections
from typing import List
from common.common_function import test_result_2


# Solution 1: Using brute force
def max_sliding_window_1(nums: List[int], k: int) -> List[int]:
    if not nums:
        return nums

    r = []

    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i + k]))

    return r


# Solution 2: Optimization using queues
def max_sliding_window_2(nums: List[int], k: int) -> List[int]:
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)

        if current_max == window.popleft():
            current_max = float('-inf')

    return results


function_list = [max_sliding_window_1, max_sliding_window_2]


if __name__ == "__main__":
    num_list = [1, 3, -1, -3, 5, 3, 6, 7]
    num_k = 3
    test_result_2('Numbers', function_list, num_list, num_k)
