"""
    Problem 17: Swap Nodes in Pairs

    Question: Swap given linked list in pairs
    Source: leetcode 24 (https://leetcode.com/problems/swap=nodes-in-pairs/

"""
from common.common_function import ListNode, create_linked_list, test_result_single


# Solution 1: Exchanging values of nodes
def swap_pairs_1(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next_node:
        cur.val, cur.next_node.val = cur.next_node.val, cur.val
        cur = cur.next_node.next_node

    return head


# Solution 2: Swap by repetitive structure
def swap_pairs_2(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next_node:
        b = head.next_node
        head.next_node = b.next_node
        b.next_node = head

        prev.next_node = b

        head = head.next_node
        prev = prev.next_node.next_node

    return root.next_node


# Solution 3: Swap by recursion
def swap_pairs_3(head: ListNode) -> ListNode:
    if head and head.next_node:
        p = head.next_node
        head.next_node = swap_pairs_3(p.next_node)
        p.next_node = head
        return p
    return head


function_list = [swap_pairs_1, swap_pairs_2, swap_pairs_3]


if __name__ == "__main__":
    linked_lists_1 = [create_linked_list([1, 2, 3, 4]) for i in range(len(function_list))]
    print(f'Given Linked_list Info: {linked_lists_1[0]}')
    result_lists = [test_result_single(i, function_list, linked_lists_1[i]) for i in range(len(function_list))]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
