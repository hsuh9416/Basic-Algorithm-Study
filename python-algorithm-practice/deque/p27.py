"""
    Problem 27: Merge k Sorted Lists

    Question: Merge k sorted lists to one sorted list
    Source: leetcode 23 (https://leetcode.com/problems/merge-k-sorted-lists/

"""
import heapq

from common.common_function import create_linked_list, test_result_single, ListNode


# Solution: Using priority queue
def merge_k_list(lists: list[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next_node = node[2]

        result = result.next_node
        if result.next_node:
            heapq.heappush(heap, (result.next_node.val, idx, result.next_node))

    return root.next_node


function_list = [merge_k_list]

if __name__ == "__main__":
    linked_lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    for i in linked_lists:
        print(f'Given Linked_list Info: {i}')
    print()
    test_result_single(0, function_list, linked_lists)
