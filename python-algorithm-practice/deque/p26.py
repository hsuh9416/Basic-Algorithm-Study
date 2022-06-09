"""
    Problem 26: Design Circular Deque

    Question: Design a circular deque that applies following function
    * following function list:
        MyCircularDeque(k), insertFront(), insertLast(), deleteFront(), deleteLast(),
        getFront(), getRear(), isEmpty(), isFull()
    Source: leetcode 641 (https://leetcode.com/problems/design-circular-deque/
"""
from typing import Any
from common.common_function import test_function, ListNode


# Solution: Using bidirectional linked list
class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insert_front(self, value: Any) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insert_last(self, value: Any) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def delete_front(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def delete_last(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def get_front(self) -> int:
        return self.head.right.val if self.len else -1

    def get_rear(self) -> int:
        return self.tail.left.val if self.len else -1

    def is_empty(self) -> bool:
        return self.len == 0

    def is_full(self) -> bool:
        return self.len == self.k


if __name__ == "__main__":
    circularQueue = MyCircularDeque(3)
    test_function('insertLast', circularQueue.insert_last, 1)
    test_function('insertLast', circularQueue.insert_last, 2)
    test_function('insertFront', circularQueue.insert_front, 3)
    test_function('insertFront', circularQueue.insert_front, 4)
    test_function('getRear', circularQueue.get_rear)
    test_function('isFull', circularQueue.is_full)
    test_function('deleteLast', circularQueue.delete_last)
    test_function('insertFront', circularQueue.insert_front, 4)
    test_function('getFront', circularQueue.get_front)
