"""
    Problem 8. Trapping Rain Water

    Question: Calculate accumulate amount of water trapped by given height information
    Source: leetcode 42 (https://leetcode.com/problems/trapping-rain-water/

"""
import time
from typing import List


# Solution 1: Using two pointer
def trap_1(heights: List[int]) -> int:
    if not heights:
        return 0

    volume = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]

    while left < right:
        left_max, right_max = max(heights[left], left_max), max(heights[right], right_max)

        if left_max <= right_max:
            volume += left_max - heights[left]
            left += 1
        else:
            volume += right_max - heights[right]
            right -= 1

    return volume


# Solution 2: Using stack
def trap_2(heights: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(heights[i], heights[stack[-1]]) - heights[top]

            volume += distance * waters

        stack.append(i)

    return volume


function_list = [trap_1, trap_2]


def test_result(arg_type: str, func_list: List, arg_val: List[int]) -> None:
    print(f'Given {arg_type} Info: {arg_val}')
    result_time = []
    for i in range(len(func_list)):
        print()

        start = time.perf_counter()
        result = func_list[i](arg_val)
        end = time.perf_counter()
        time_elapsed = end - start

        print(f'Solution {i + 1} Result: {result}')
        print(f'Solution {i + 1}  Time elapsed: {time_elapsed}')

        result_time.append(time_elapsed)

    print(f"Solution {result_time.index(min(result_time)) + 1} was the fastest!")


if __name__ == "__main__":
    height_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    test_result('Array', function_list, height_list)
