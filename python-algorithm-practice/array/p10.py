"""
    Problem 10. Array Partition

    Question: Print out the biggest number can be created by sum of two of min(a,b) value using n pairs
    Source: leetcode 561 (https://leetcode.com/problems/array-partition-i/

"""
from typing import List
from p8 import test_result


# Solution 1: Using ascending order sort to find argmax that make min() as maximum
def array_pair_sum_1(nums: List[int]) -> int:
    result = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            result += min(pair)
            pair = []

    return result


# Solution 2: Using even index values
def array_pair_sum_2(nums: List[int]) -> int:
    result = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            result += n

    return result


# Solution 3: Pythonic method
def array_pair_sum_3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


function_list = [array_pair_sum_1, array_pair_sum_2, array_pair_sum_3]


if __name__ == "__main__":
    num_list = [1, 4, 3, 2]
    test_result('Array', function_list, num_list)
