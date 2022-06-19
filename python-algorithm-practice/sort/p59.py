"""
    Problem 59: Merge Intervals

    Question: Merge duplicated intervals
    Source: leetcode 56 (https://leetcode.com/problems/merge-intervals/

"""
from typing import List
from common.common_function import test_result_single


# Solution: Using sort
def merge(intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged.append(i)
    return merged


function_list = [merge]

if __name__ == "__main__":
    interval_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f'Given interval list Info: {interval_list}')
    test_result_single(0, function_list, interval_list)
