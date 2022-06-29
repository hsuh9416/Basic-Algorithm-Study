"""
    Problem 88: House Robber

    Question: Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police
    Source: leetcode 198 (https://leetcode.com/problems/house-robber/
"""
import collections
from typing import List

from common.common_function import test_result


# Solution 1: Using recursive brute force
def rob_1(nums: List[int]) -> int:
    def _rob(i: int) -> int:
        if i < 0:
            return 0
        return max(_rob(i - 1), _rob(i - 2) + nums[i])
    return _rob(len(nums) - 1)


# Solution 2: Using tabulation
def rob_2(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    dp = collections.OrderedDict()
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp.popitem()[1]


function_list = [rob_1, rob_2]


if __name__ == "__main__":
    num_list_1 = [1, 2, 3, 1]
    test_result('Number List', function_list, num_list_1)
    print()
    num_list_2 = [2, 7, 9, 3, 1]
    test_result('Number List', function_list, num_list_2)
