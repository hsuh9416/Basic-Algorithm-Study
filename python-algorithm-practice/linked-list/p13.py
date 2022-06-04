"""
    Problem 13: Palindrome Linked List

    Question: Determine the given linked list if it is palindrome
    Source: leetcode 234 (https://leetcode.com/problems/palindrome-linked-list/

"""


# class ListNode:
from typing import Optional
from common.common_function import test_result

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Using brute-force algorithm
def is_palindrome_1(head: Optional[ListNode]) -> bool:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price


# Solution 2: Using the difference between the low and the current value
def is_palindrome_2(head: Optional[ListNode]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


function_list = [is_palindrome_1, is_palindrome_2]

if __name__ == "__main__":
    head_1 = [1, 2, 2, 1]
    test_result('Linked List', function_list, head_1)
    print()
    head_2 = [1, 2]
    test_result('Linked List', function_list, head_2)
