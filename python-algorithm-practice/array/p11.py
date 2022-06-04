"""
    Problem 11. Product of Array Except Self

    Question: Print out all product combination of given array
        * Excludes the array itself
        * Do not divide
    Source: leetcode 238 (https://leetcode.com/problems/product-of-array-except-self/

"""
from typing import List
from common.common_function import test_result


# Solution: Multiply sequentially from left to right
def product_except_self(nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1

    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


function_list = [product_except_self]


if __name__ == "__main__":
    num_list = [1, 2, 3, 4]
    test_result('Array', function_list, num_list)
