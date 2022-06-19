"""
    Problem 58: Kth Largest Element in an Array

    Question: Sort a linked list in O(n log n)
    Source: leetcode 148 (https://leetcode.com/problems/sort-list/

"""
from common.common_function import test_result_single, create_linked_list, ListNode
from linkedlist.p14 import merge_two_lists


# Solution 1: Using merge sort
def sort_list_1(head: ListNode) -> ListNode:
    if not (head and head.next_node):
        return head

    half, slow, fast = None, head, head

    while fast and fast.next_node:
        half, slow, fast = slow, slow.next_node, fast.next_node.next_node
    half.next_node = None

    l1 = sort_list_1(head)
    l2 = sort_list_1(slow)

    return merge_two_lists(l1, l2)


# Solution 2: Using built-in function
def sort_list_2(head: ListNode) -> ListNode:
    p = head
    lst = []
    while p:
        lst.append(p.val)
        p = p.next_node

    lst.sort()

    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next_node

    return head


function_list = [sort_list_1, sort_list_2]

if __name__ == "__main__":
    linked_lists = [create_linked_list([4, 2, 1, 3]) for i in range(len(function_list))]
    print(f'Given Linked_list Info: {linked_lists[0]}')
    result_lists = [test_result_single(i, function_list, linked_lists[i]) for i in range(len(function_list))]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
