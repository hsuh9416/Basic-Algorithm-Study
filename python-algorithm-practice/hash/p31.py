"""
    Problem 31: Top K Frequent Elements

    Question: Extract top K frequent elements from given number list
    Source: leetcode 347 (https://leetcode.com/problems/top-k-frequent-elements/

"""
import collections
import heapq
from typing import List
from common.common_function import test_result_2


# Solution 1: Using counter
def top_k_frequent_1(nums: List[int], k: int) -> List[int]:
    freq_s = collections.Counter(nums)
    freq_s_heap = []

    for f in freq_s:
        heapq.heappush(freq_s_heap, (-freq_s[f], f))

    top_k = list()

    for _ in range(k):
        top_k.append(heapq.heappop(freq_s_heap)[1])

    return top_k


# Solution 2: Using pythonic method
def top_k_frequent_2(nums: List[int], k: int):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


function_list = [top_k_frequent_1, top_k_frequent_2]


if __name__ == "__main__":
    num_list = [1, 1, 1, 2, 2, 3]
    k_freq = 2
    test_result_2('Numbers', function_list, num_list, k_freq)
