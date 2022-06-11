"""
    Problem 35: Combinations

    Question: Return k numbers of combinations using given total number n
    Source: leetcode 77 (https://leetcode.com/problems/combinations/

"""
import itertools
from typing import List, Any
from common.common_function import test_result_2


# Solution 1: Create combinations by DFS
def combine_1(num_n: int, num_k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        for i in range(start, num_n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, num_k)
    return results


# Solution 2: Using itertools module
def combine_2(num_n: int, num_k: int) -> List[tuple[Any]]:
    return list(itertools.combinations(range(1, num_n + 1), num_k))


function_list = [combine_1, combine_2]


if __name__ == "__main__":
    total_num = 4
    total_combinations = 2
    test_result_2('Numbers', function_list, total_num, total_combinations)
