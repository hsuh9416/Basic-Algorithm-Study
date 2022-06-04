"""
    Problem 15: Reverse Linked List

    Question: Reverse the given linked list
    Source: leetcode 206 (https://leetcode.com/problems/reverse-linked-list/

"""
from common.common_function import ListNode, create_linked_list, test_result_single


# Solution 1: Using recursion
def reverse_list_1(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        reversed_next, node.next_node = node.next_node, prev
        return reverse(reversed_next, node)
    return reverse(head)


# Solution 2: Using respective structure
def reverse_list_2(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next_node, node.next_node = node.next_node, prev
        prev, node = node, next_node

    return prev


function_list = [reverse_list_1, reverse_list_2]


if __name__ == "__main__":
    linked_lists = [create_linked_list([1, 2, 3, 4, 5]) for i in range(len(function_list))]
    print(f'Given Linked_list Info: {linked_lists[0]}')
    result_list = [test_result_single(0, function_list, linked_lists[i]) for i in range(len(function_list))]
    print(f"Solution {result_list.index(min(result_list)) + 1} was the fastest!")
