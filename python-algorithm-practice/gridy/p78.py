"""
    Problem 78: Best Time to Buy and Sell Stock II

    Question: Calculate the maximum profit you can make from multiple trades
    Source: leetcode 122 (https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List
from common.common_function import test_result


# Solution 1: Greedy algorithm
def max_profit_1(prices: List[int]) -> int:
    result = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result


# Solution 2: Pythonic method
def max_profit_2(prices: List[int]) -> int:
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


function_list = [max_profit_1, max_profit_2]


if __name__ == "__main__":
    num_list = [7, 1, 5, 3, 6, 4]
    test_result('Strings', function_list, num_list)
