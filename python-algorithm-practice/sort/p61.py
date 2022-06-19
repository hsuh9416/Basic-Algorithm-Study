"""
    Problem 61: Largest Number

    Question: Print the largest number that can be made by combining the items
    Source: leetcode 179 (https://leetcode.com/problems/largest-number/

"""
from typing import List
from common.common_function import test_result_single


# Solution: Using insertion sort
class Solution:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largest_number(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


function_list = [Solution().largest_number]

if __name__ == "__main__":
    given_list_1 = [10, 2]
    print(f'Given list Info: {given_list_1}')
    test_result_single(0, function_list, given_list_1)
    given_list_2 = [3, 30, 34, 5, 9]
    print(f'Given list Info: {given_list_2}')
    test_result_single(0, function_list, given_list_2)
