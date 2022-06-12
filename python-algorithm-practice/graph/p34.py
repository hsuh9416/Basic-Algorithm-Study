"""
    Problem 34: Permutations

    Question: Take different integers and return all possible permutations
    Source: leetcode 46 (https://leetcode.com/problems/permutations/

"""
import itertools
from typing import List
from common.common_function import test_result


# Solution 1: Create permutations by DFS
def permute_1(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


# Solution 2: Using itertools module
def permute_2(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))


function_list = [permute_1, permute_2]


if __name__ == "__main__":
    num_list = [1, 2, 3]
    test_result('Numbers', function_list, num_list)
