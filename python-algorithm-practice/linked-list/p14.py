"""
    Problem 14: Merge Two Sorted Lists

    Question: Merge two given sorted list
    Source: leetcode 21 (https://leetcode.com/problems/merge-two-sorted-lists/

"""
from common.common_function import create_linked_list, ListNode, test_result_2


# Solution 1: Using recursion
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if not(l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next_node = merge_two_lists(l1.next_node, l2)
    return l1


function_list = [merge_two_lists]

if __name__ == "__main__":
    linked_list_1 = create_linked_list([1, 2, 4])
    linked_list_2 = create_linked_list([1, 3, 4])

    test_result_2('Linked Lists', function_list, linked_list_1, linked_list_2)
