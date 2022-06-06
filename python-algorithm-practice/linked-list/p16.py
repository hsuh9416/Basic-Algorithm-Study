"""
    Problem 16: Add Two Numbers

    Question: Add the numbers of linked lists that stored in reversed order
    Source: leetcode 2 (https://leetcode.com/problems/add-two-numbers/

"""

from common.common_function import ListNode, create_linked_list, linkedlist_to_list, test_result_single
from p15 import reverse_list_2


# Solution 1: Using data type transformation
def add_two_numbers_1(l1: ListNode, l2: ListNode) -> ListNode:
    a = linkedlist_to_list(reverse_list_2(l1))
    b = linkedlist_to_list(reverse_list_2(l2))

    result_str = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

    result_list = [int(i) for i in str(result_str)]

    return reverse_list_2(create_linked_list(result_list))


# Solution 2: Using full adder implementation
def add_two_numbers_2(l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum_l = 0
        if l1:
            sum_l += l1.val
            l1 = l1.next_node
        if l2:
            sum_l += l2.val
            l2 = l2.next_node

        carry, val = divmod(sum_l + carry, 10)
        head.next_node = ListNode(val)
        head = head.next_node

    return root.next_node


function_list = [add_two_numbers_1, add_two_numbers_2]

if __name__ == "__main__":
    linked_lists_1 = [create_linked_list([2, 4, 3]) for i in range(len(function_list))]
    linked_lists_2 = [create_linked_list([5, 6, 4]) for i in range(len(function_list))]
    print(f'Given Linked_list Info: {linked_lists_1[0]} {linked_lists_2[0]}')
    result_lists = [test_result_single(i, function_list, linked_lists_1[i], linked_lists_2[i])
                    for i in range(len(function_list))]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
