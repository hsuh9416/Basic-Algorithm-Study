"""
    Problem 40: Network Delay Time

    Question: Starting from K, calculate the amount of time that all nodes can receive a signal
    * Conditions and Instructions
        1) If not possible, -1 is returned
        2) The input values (u, v, w) are each composed of a departure point, a destination, and a required time
        3) The total number of nodes should be a given input N
    Source: leetcode 743 (https://leetcode.com/problems/network-delay-time/

"""
import collections
import heapq
from typing import List
from common.common_function import test_result_single


# Solution: Using Dijkstra
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    q = [(0, k)]
    dist = collections.defaultdict(int)

    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

    if len(dist) == n:
        return max(dist.values())
    return -1


function_list = [network_delay_time]


if __name__ == "__main__":
    input_times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    input_N = 4
    input_K = 2
    print(f'Given Input Info: times = {input_times}, N = {input_N}, K = {input_K}', end='\n\n')
    test_result_single(0, function_list, input_times, input_N, input_K)
