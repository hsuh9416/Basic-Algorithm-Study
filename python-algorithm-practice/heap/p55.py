"""
    Problem 55: Kth Largest Element in an Array

    Question: Extract the kth largest element from an unsorted array
    Source: leetcode 215 (https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
import heapq
from typing import List
from common.common_function import test_result_single


# Solution 1: Using heapq module
def find_kth_largest_1(nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(1, k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)


# Solution 2: Using heapify in heapq module
def find_kth_largest_2(nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


# Solution 3: Using nlargest in heapq module
def find_kth_largest_3(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


# Solution 4: Using sort
def find_kth_largest_4(nums: List[int], k: int) -> int:
    nums.reverse()
    return nums[k - 1]


function_list = [find_kth_largest_1, find_kth_largest_2, find_kth_largest_3, find_kth_largest_4]

if __name__ == "__main__":
    list_len = len(function_list)
    num_lists = [[3, 2, 3, 1, 2, 4, 5, 5, 6] for i in range(len(function_list))]
    num_ks = [4 for i in range(len(function_list))]
    print(f"Given Input Info: nums = {num_lists[0]}, k = {num_ks[0]}", end='\n\n')
    result_lists = [test_result_single(i, function_list, num_lists[i], num_ks[i]) for i in range(len(function_list))]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
