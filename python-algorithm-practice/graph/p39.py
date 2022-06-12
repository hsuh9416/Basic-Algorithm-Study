"""
    Problem 39: Course Schedule

    Question: Determine whether all courses are complete
    * Conditions
        1) There are n courses that represent the pair of [0,1] that one must finish in order to complete zero
        2) iven the number of courses n and these pairs as input

    Source: leetcode 207 (https://leetcode.com/problems/course-schedule/

"""
import collections
from typing import List
from common.common_function import test_result


# Solution 1: Determine cyclic structure by using DFS
def can_finish_1(prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        if i in traced:
            return False

        traced.add(i)

        for s_y in graph[i]:
            if not dfs(s_y):
                return False

        traced.remove(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True


# Solution 2: Using branches to optimize
def can_finish_2(prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        if i in traced:
            return False

        if i in visited:
            return True

        traced.add(i)

        for s_y in graph[i]:
            if not dfs(s_y):
                return False

        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True


function_list = [can_finish_1, can_finish_2]


if __name__ == "__main__":
    input_list_1 = [[1, 0]]
    test_result('number of course, list of pairs', function_list, input_list_1)
    print()
    input_list_2 = [[1, 0], [0, 1]]
    test_result('number of course, list of pairs', function_list, input_list_2)
