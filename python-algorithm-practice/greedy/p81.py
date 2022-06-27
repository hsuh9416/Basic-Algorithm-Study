"""
    Problem 81: Gas Station

    Question: Given two integer arrays gas and cost, return the starting gas station's index
    if you can travel around the circuit once in the clockwise direction, otherwise return -1
    Source: leetcode 134 (https://leetcode.com/problems/gas-station/
"""
from typing import List
from common.common_function import test_result_2


# Solution 1: Visit all gas station
def can_complete_circuit_1(gas: List[int], cost: List[int]) -> int:
    can_travel = None
    for start in range(len(gas)):
        fuel = 0
        for i in range(start, len(gas) + start):
            index = i % len(gas)

            can_travel = True
            if gas[index] + fuel < cost[index]:
                can_travel = False
                break
            else:
                fuel += gas[index] - cost[index]
        if can_travel:
            return start
    return -1


# Solution 2: Visit just one gas station
def can_complete_circuit_2(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0
    for i in range(len(gas)):
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]

    return start


function_list = [can_complete_circuit_1, can_complete_circuit_2]


if __name__ == "__main__":
    gas_list = [1, 2, 3, 4, 5]
    cost_list = [3, 4, 5, 1, 2]
    test_result_2('Number List', function_list, gas_list, cost_list)
