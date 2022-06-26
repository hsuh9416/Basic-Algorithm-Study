"""
    Problem 79: Queue Reconstruction by Height

    Question: Several people are lining up
    Each person has two integer pairs of (h, k), where h is the person's height and k is the number of people
    in the queue who are taller than themselves
    Write an algorithm to rearrange the lines so that this value is correct
    Source: leetcode 406 (https://leetcode.com/problems/queue-reconstruction-by-height/
"""
import heapq
from typing import List
from common.common_function import test_result


# Solution 1: Using queue
def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    heap = []
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))

    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])

    return result


function_list = [reconstruct_queue]


if __name__ == "__main__":
    num_list = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    test_result('Number List', function_list, num_list)
