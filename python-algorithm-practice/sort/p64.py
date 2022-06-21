"""
    Problem 64: The Kth Closest Points to Origin

    Question: print the list of points K closest to the origin (0, 0) in order by a list of points on the plane.
    * The distance between two points on a plane is the Euclidean distance.
    Source: leetcode 973 (https://leetcode.com/problems/k-closest-points-to-origin/

"""
import heapq
from typing import Any, List
from common.common_function import test_result_single


# Solution: Applying Euclidean Distance
def k_closest(points: List[List[int]], k: int) -> Any:
    heap = []
    for (x, y) in points:
        dist = x ** 2 + y ** 2
        heapq.heappush(heap, (dist, x, y))

    result = []
    for _ in range(k):
        (dist, x, y) = heapq.heappop(heap)
        result.append((x, y))
    return result


function_list = [k_closest]


if __name__ == "__main__":
    list_points_1 = [[1, 3], [-2, 2]]
    num_k_1 = 1
    print(f"Given Input Info: points = {list_points_1}, K = {num_k_1}", end='\n\n')
    test_result_single(0, function_list, list_points_1, num_k_1)
    print()
    list_points_2 = [[3, 3], [5, -1], [-2, 4]]
    num_k_2 = 2
    print(f"Given Input Info: points = {list_points_2}, K = {num_k_2}", end='\n\n')
    test_result_single(0, function_list, list_points_2, num_k_2)
