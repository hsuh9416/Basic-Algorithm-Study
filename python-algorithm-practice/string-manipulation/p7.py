"""
    Problem 7. Two Sum

    Question: Return the indexes of two number, sum of which equals given target number, from the given array
    Source: leetcode 1 (https://leetcode.com/problems/two-sum/

"""
import time
from typing import List


# Solution 1: Using brute-force algorithm
def two_sum_1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Solution 2: Using 'in'
def two_sum_2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# Solution 3: Using key searching
def two_sum_3(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):

        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
        nums_map[num] = i


# Solution 4: Using two pointer
def two_sum_4(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


function_list = [two_sum_1, two_sum_2, two_sum_3, two_sum_4, ]


def test_result(nums: List[int], target: int) -> None:
    print(f'Given Array: {nums}, Target Number = {target}')
    result_time = []
    for i in range(len(function_list)):
        print()

        start = time.perf_counter()
        result = function_list[i](nums, target)
        end = time.perf_counter()
        time_elapsed = end - start

        print(f'Solution {i + 1} Result: {result}')
        print(f'Solution {i + 1}  Time elapsed: {time_elapsed}')

        result_time.append(time_elapsed)

    print(f"Solution {result_time.index(min(result_time)) + 1} was the fastest!")


if __name__ == "__main__":
    num_list = [2, 7, 11, 15]
    target_num = 9
    test_result(num_list, target_num)
