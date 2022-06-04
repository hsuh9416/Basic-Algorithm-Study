"""
    Problem 9. 3Sum

    Question: Print out all combinations of three elements that sum to zero
    Source: leetcode 15 (https://leetcode.com/problems/3sum/

"""
from typing import List
from common.common_function import test_result


# Solution 1: Using brute-force algorithm
def three_sum_1(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


# Solution 2: Using two pointer
def three_sum_2(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum_num = nums[i] + nums[left] + nums[right]
            if sum_num < 0:
                left += 1
            elif sum_num > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


function_list = [three_sum_1, three_sum_2]

if __name__ == "__main__":
    num_list = [-1, 0, 1, 2, -1, -4]

    test_result('Array', function_list, num_list)
