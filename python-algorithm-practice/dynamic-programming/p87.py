"""
    Problem 87: Climbing Stairs

    Question: Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Source: leetcode 70 (https://leetcode.com/problems/climbing-stairs/
"""
import collections
from common.common_function import test_result


# Solution 1: Using recursive brute force
def climb_stairs_1(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_1(n - 1) + climb_stairs_1(n - 2)


# Solution 2: Using memoization
class Solution:
    dp = collections.defaultdict(int)

    def climb_stairs_2(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climb_stairs_2(n - 1) + self.climb_stairs_2(n - 2)
        return self.dp[n]


function_list = [climb_stairs_1, Solution().climb_stairs_2]


if __name__ == "__main__":
    n_1 = 2
    test_result('Number', function_list, n_1)
    print()
    n_2 = 3
    test_result('Number', function_list, n_2)
