"""
    Problem 84: Different Ways to Add Parentheses

    Question: Take numbers and operators as input and print the results of all possible combinations
    Source: leetcode 241 (https://leetcode.com/problems/different-ways-to-add-parentheses/
"""
from typing import List
from common.common_function import test_result


# Solution 1: Using divide and conquer
def diff_ways_to_compute(input_str: str) -> List[int]:
    def compute(s_left, s_right, op):
        s_results = []
        for lf in s_left:
            for r in s_right:
                s_results.append(eval(str(lf) + op + str(r)))
        return s_results

    if input_str.isdigit():
        return [int(input_str)]

    results = []
    for index, value in enumerate(input_str):
        if value in "-+*":
            left = diff_ways_to_compute(input_str[:index])
            right = diff_ways_to_compute(input_str[index + 1:])

            results.extend(compute(left, right, value))

    return results


function_list = [diff_ways_to_compute]


if __name__ == "__main__":
    str_list_1 = "2-1-1"
    test_result('String', function_list, str_list_1)
    print()
    str_list_2 = "2*3-4*5"
    test_result('String', function_list, str_list_2)
