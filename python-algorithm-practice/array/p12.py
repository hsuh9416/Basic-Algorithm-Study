"""
    Problem 12: Best Time to Buy and Sell Stock

    Question: Calculate the maximum profit can achieve from single transaction
    Source: leetcode 121 (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
import sys
from typing import List
from common.common_function import test_result


# Solution 1: Using brute-force algorithm
def max_profit_1(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# Solution 2: Using the difference between the low and the current value
def max_profit_2(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


function_list = [max_profit_1, max_profit_2]


if __name__ == "__main__":
    num_list = [7, 1, 5, 3, 6, 4]
    test_result('Price List', function_list, num_list)
