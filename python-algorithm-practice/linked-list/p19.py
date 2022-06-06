"""
    Problem 19: Reverse Linked List II

    Question: Reverse the given linked list from index m to index n; m starts from 1
    Source: leetcode 92 (https://leetcode.com/problems/reverse-linked-list-ii/

"""
from common.common_function import create_linked_list, ListNode, test_result_single


# Solution: Using repetitive structure
def reverse_between(head: ListNode, idx_range: tuple) -> ListNode:
    if not head or idx_range[0] == idx_range[1]:
        return head

    root = start = ListNode(None)
    root.next_node = head
    for _ in range(idx_range[0] - 1):
        start = start.next_node
    end = start.next_node

    for _ in range(idx_range[1] - idx_range[0]):
        tmp, start.next_node, end.next_node = start.next_node, end.next_node, end.next_node.next_node
        start.next_node.next_node = tmp

    return root.next_node


function_list = [reverse_between]


if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    start_idx, end_idx = 2, 4
    print(f'Given Linked_list Info: {linked_list}, Given Index Range = ({start_idx},{end_idx})')
    test_result_single(0, function_list, linked_list, (start_idx, end_idx))
