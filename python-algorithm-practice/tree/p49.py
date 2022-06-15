"""
    Problem 49: Minimum Height Tree

    Question: Return a list of roots for which the tree has the minimum height by given node number and undirected graph
    Source: leetcode 310 (https://leetcode.com/problems/minimum-height-tree/

"""
import collections
from typing import List
from common.common_function import test_result_single


# Solution: Step by step leef node removal
def find_min_height_trees(n: int, edges: List[List[int]]) -> List[int]:
    if n <= 1:
        return [0]

    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    leaves = []

    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves

    return leaves


function_list = [find_min_height_trees]


if __name__ == "__main__":
    num_1 = 4
    edges_1 = [[1, 0], [1, 2], [1, 3]]
    print(f"Given Input Info: n = {num_1}, edges = {edges_1}", end='\n\n')
    test_result_single(0, function_list, num_1, edges_1)
    print()
    num_2 = 6
    edges_2 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    print(f"Given Input Info: n = {num_2}, edges = {edges_2}", end='\n\n')
    test_result_single(0, function_list, num_2, edges_2)
