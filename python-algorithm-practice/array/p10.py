"""
    Problem 10. Array Partition

    Question: Print out the biggest number can be created by sum of two of min(a,b) value using n pairs
    Source: leetcode 561 (https://leetcode.com/problems/array-partition-i/

"""
import time
from typing import List


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


def test_result(nums: List[int]) -> None:
    print(f'Given Array Info: {nums}')

    result_time = []

    for i in range(len(function_list)):
        start = time.perf_counter()
        result = function_list[i](nums)
        end = time.perf_counter()
        time_elapsed = end - start

        print(f'Solution {i + 1} Result: {result}')
        print(f'Solution {i + 1}  Time elapsed: {time_elapsed}', end="\n\n")

        result_time.append(time_elapsed)

    print(f"Solution {result_time.index(min(result_time)) + 1} was the fastest!")


if __name__ == "__main__":
    num_list = [1, 4, 3, 2]
    test_result(num_list)
