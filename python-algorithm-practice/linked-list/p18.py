"""
    Problem 18: Odd Even Linked List

    Question: Reorganize the linked list so that odd nodes are followed by even nodes
    * Solve As: Space Complexity -> O(1), Time Complexity -> O(n)
    Source: leetcode 328 (https://leetcode.com/problems/odd-even-linked-list/

"""
from typing import Any
from common.common_function import create_linked_list, ListNode, test_result_single


# Solution: Using repetitive structure
def odd_even_list(head: ListNode) -> Any:
    if head is None:
        return None

    odd = head
    even = head.next_node
    even_head = head.next_node

    while even and even.next_node:
        odd.next_node, even.next_node = odd.next_node.next_node, even.next_node.next_node
        odd, even = odd.next_node, even.next_node

    odd.next_node = even_head
    return head


function_list = [odd_even_list]


if __name__ == "__main__":
    linked_list_1 = create_linked_list([1, 2, 3, 4, 5])
    print(f'Given Linked_list 1 Info: {linked_list_1}')
    test_result_single(0, function_list, linked_list_1)
    print()
    linked_list_2 = create_linked_list([2, 1, 3, 5, 6, 4, 7])
    print(f'Given Linked_list 2 Info: {linked_list_2}')
    test_result_single(0, function_list, linked_list_2)





