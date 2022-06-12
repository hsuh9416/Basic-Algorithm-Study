"""
    Problem 38: Reconstruct Itinerary

    Question: Organize the itinerary from JFK using a list of tickets consisting of [from, to]
    * If there are multiple schedules, visit in lexical order
    Source: leetcode 332 (https://leetcode.com/problems/reconstruct-itinerary/

"""
import collections
from typing import List
from common.common_function import test_result


# Solution 1: Organize graph by using DFS
def find_itinerary_1(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(s_a):
        while graph[s_a]:
            dfs(graph[s_a].pop(0))
        route.append(s_a)

    dfs('JFK')

    return route[::-1]


# Solution 2: Using stack operation to optimize queue operation
def find_itinerary_2(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(s_a):
        while graph[s_a]:
            dfs(graph[s_a].pop(0))
        route.append(s_a)

    dfs('JFK')

    return route[::-1]


# Solution 3: Repeating of itinerary graph
def find_itinerary_3(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]


function_list = [find_itinerary_1, find_itinerary_2, find_itinerary_3]


if __name__ == "__main__":
    input_list_1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    test_result('Number List', function_list, input_list_1)
    print()
    input_list_2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    test_result('Number List', function_list, input_list_2)
