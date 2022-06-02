"""
    Problem 11. Product of Array Except Self

    Question: Print out all product combination of given array
        * Excludes the array itself
    Source: leetcode 238 (https://leetcode.com/problems/product-of-array-except-self/

"""
from typing import List
from p8 import test_result


# Solution: Using ascending order sort to find argmax that make min() as maximum
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