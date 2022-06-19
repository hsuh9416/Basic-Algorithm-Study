"""
    Problem 60: Insertion Sort List

    Question: Sort a linked list using insertion sort

    Source: leetcode 147 (https://leetcode.com/problems/sort-list/

"""
from common.common_function import test_result_single, create_linked_list, ListNode


# Solution 1: Using basic insertion sort
def insertion_sort_list_1(head: ListNode) -> ListNode:
    cur = parent = ListNode(None)
    while head:
        while cur.next_node and cur.next_node.val < head.val:
            cur = cur.next_node

        cur.next, head.next_node, head = head, cur.next_node, head.next_node

        cur = parent

    return cur.next_node


# Solution 2: Using advanced insertion sort
def insertion_sort_list_2(head: ListNode) -> ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next_node and cur.next_node.val < head.val:
            cur = cur.next_node

        cur.next, head.next_node, head = head, cur.next_node, head.next_node

        if head and cur.val > head.val:
            cur = parent

    return parent.next_node


function_list = [insertion_sort_list_1, insertion_sort_list_2]


if __name__ == "__main__":
    linked_lists = [create_linked_list([4, 2, 1, 3]) for i in range(len(function_list))]
    print(f'Given Linked_list Info: {linked_lists[0]}')
    result_lists = [test_result_single(i, function_list, linked_lists[i]) for i in range(len(function_list))]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
