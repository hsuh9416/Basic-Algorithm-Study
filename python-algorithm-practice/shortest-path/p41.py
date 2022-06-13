"""
    Problem 41: Cheapest Flights Within K Stops

    Question: Calculate the cheapest price from the starting point to the ending point of which arrives within K stops
    * If the path does not exist, return -1
    Source: leetcode 787 (https://leetcode.com/problems/cheapest-filights-within-k-stops/

"""
import collections
import heapq
from typing import List
from common.common_function import test_result_single


# Solution: Using Dijkstra
def find_cheapest_price(flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    q = [(0, src, k)]

    while q:
        price, node, k = heapq.heappop(q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(q, (alt, v, k - 1))

    return -1


function_list = [find_cheapest_price]


if __name__ == "__main__":
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    input_src = 0
    input_dst = 2
    input_K = 0
    print(f'Given Input Info: edges = {edges}, src = {input_src}, dst = {input_dst}, K = {input_K}')
    print()
    test_result_single(0, function_list, edges, input_src, input_dst, input_K)
