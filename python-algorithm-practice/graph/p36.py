"""
    Problem 36: Combination Sum

    Question: List the elements whose sum is the target by combining the number set candidates
        * Each element can be duplicated
    Source: leetcode 39 (https://leetcode.com/problems/combinations-sum/

"""
from typing import List
from common.common_function import test_result_2


# Solution: Search duplicable combination graph using DFS
def combination_sum(can: List[int], tar: int) -> List[List[int]]:
    result = []

    def dfs(c_sum, index, path):
        if c_sum < 0:
            return
        if c_sum == 0:
            result.append(path)
            return
        for i in range(index, len(can)):
            dfs(c_sum - can[i], i, path + [can[i]])
    dfs(tar, 0, [])
    return result


function_list = [combination_sum]


if __name__ == "__main__":
    candidates_1 = [2, 3, 6, 7]
    target_1 = 7
    test_result_2('Numbers', function_list, candidates_1, target_1)
    print()
    candidates_2 = [2, 3, 5]
    target_2 = 8
    test_result_2('Numbers', function_list, candidates_2, target_2)
