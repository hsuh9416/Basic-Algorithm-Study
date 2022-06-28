"""
    Problem 85: Fibonacci Number

    Question: Find the fibonacci Number
    Source: leetcode 509 (https://leetcode.com/problems/fibonacci-number/
"""
import collections
from common.common_function import test_result


# Solution 1: Using brute force
def fib_1(n: int) -> int:
    if n <= 1:
        return n
    return fib_1(n - 1) + fib_1(n - 2)


# Solution 2: Using memoization
class Solution:
    dp = collections.defaultdict(int)

    def fib_2(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib_2(n - 1) + self.fib_2(n - 2)
        return self.dp[n]


# Solution 3: Using tabulation
class Solution2:
    dp = collections.defaultdict(int)

    def fib_3(self, n: int) -> int:
        self.dp[0] = 1
        self.dp[1] = 1

        for i in range(2, n):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n - 1]


# Solution 4: Using two variable
def fib_4(n: int) -> int:
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x


function_list = [fib_1, Solution().fib_2, Solution2().fib_3, fib_4]


if __name__ == "__main__":
    num = 10
    test_result('Number', function_list, num)
