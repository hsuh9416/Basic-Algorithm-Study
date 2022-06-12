"""
    Problem 37: Subsets

    Question: Return all subsets from given list
    Source: leetcode 78 (https://leetcode.com/problems/subsets/

"""
from typing import List
from common.common_function import test_result


# Solution: Tree searching using DFS
def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


function_list = [subsets]


if __name__ == "__main__":
    num_list = [1, 2, 3]
    test_result('Number List', function_list, num_list)
