"""
    Problem 13: Palindrome Linked List

    Question: Determine the given linked list if it is palindrome
    Source: leetcode 234 (https://leetcode.com/problems/palindrome-linked-list/

"""


# class ListNode:
import collections
from typing import Optional, Any
from common.common_function import test_result


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        linked_list = self
        object_print = '['
        while True:
            object_print += str(linked_list.val)
            if linked_list.next_node is None:
                break
            object_print += '->'
            linked_list = linked_list.next_node
        return object_print + ']'


def create_linked_list(head: list, idx=-1) -> Any:

    if idx == len(head) - 1:
        return None
    else:
        return ListNode(head[idx + 1], create_linked_list(head, idx + 1))


# Solution 1: Using list conversion
def is_palindrome_1(head: Optional[ListNode]) -> bool:
    q = []

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next_node

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# Solution 2: Using Deque
def is_palindrome_2(head: Optional[ListNode]) -> bool:
    q = collections.deque()

    if not head:
        return True

    node = head

    while node is not None:
        q.append(node.val)
        node = node.next_node

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# Solution 3: Using Runner
def is_palindrome_3(head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        rev, rev.next, slow = slow, rev, slow.next_node
    if fast:
        slow = slow.next_node

    while rev and rev.val == slow.val:
        slow, rev = slow.next_node, rev.next_node

    return not rev


function_list = [is_palindrome_1, is_palindrome_2, is_palindrome_3]


if __name__ == "__main__":

    head_1 = [1, 2, 2, 1]
    linked_list_1 = create_linked_list(head_1)

    test_result('Linked List', function_list, linked_list_1)
    print()
    head_2 = [1, 2]
    linked_list_2 = create_linked_list(head_2)
    test_result('Linked List', function_list, linked_list_2)
