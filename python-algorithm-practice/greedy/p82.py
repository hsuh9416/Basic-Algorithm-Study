"""
    Problem 82: Assign Cookies

    Question: Maximize the number of your content children and output the maximum number.
    Source: leetcode 455 (https://leetcode.com/problems/assign-cookies/
"""
from typing import List
from bisect import bisect_right
from common.common_function import test_result_2


# Solution 1: Using greedy algorithm
def find_content_children_1(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    child_i = cookie_j = 0
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1

    return child_i


# Solution 2: Using binary search
def find_content_children_2(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    result = 0
    for i in s:
        index = bisect_right(g, i)
        if index > result:
            result += 1
    return result


function_list = [find_content_children_1, find_content_children_2]


if __name__ == "__main__":
    g_1 = [1, 2, 3]
    s_1 = [1, 1]
    test_result_2('Number List', function_list, g_1, s_1)
    print()
    g_2 = [1, 2]
    s_2 = [1, 2, 3]
    test_result_2('Number List', function_list, g_2, s_2)
