"""
    Problem 63: Sort Colors

    Question: When red is 0, white is 1, and blue is 2, perform adjacent in-place sorting in that order
    Source: leetcode 75 (https://leetcode.com/problems/sort-colors/

"""
from typing import List
from common.common_function import test_result


# Solution: Applying Dutch National Flag Problem
def sort_colors_1(nums: List[int]) -> None:
    red, white, blue = 0, 9, len(nums)

    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1


function_list = [sort_colors_1]

if __name__ == "__main__":
    num_lists = [2, 0, 2, 1, 1, 0]
    test_result("List", function_list, num_lists)
