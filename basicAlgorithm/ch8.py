"""
    Ch8 List(리스트)
    * Skipped too simple examples

    * important notes
    1) Linked list: List data type connects node to node like chaining
        => Also called as 'linear list'
        => Properties of node: Element(Value), Pointer(Connector to next node)
        => Head node: The first node
           Tail node: The last connected node
           Predecessor node: The previous node
           Successor node: The next node
        => 'List' type of Python is not a data type of list: Actually it is 'Array'

"""
from __future__ import annotations
from typing import Any


class Node:

    def __init__(self, data: Any = None, successor: Node = None):
        """ Initialize """
        self.data = data  # Data
        self.successor = successor  # Successor node


class LinkedList:

    def __init__(self) -> None:
        """ Initialize """
        self.no = 0  # Number of node
        self.head = None  # Head node
        self.current = None  # Current node

    def __len__(self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        ptr = self.head
        self.head = self.current = Node(data, ptr)  # Set original head node to next node than store
        self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.successor is not None:  # Proceed until the end
                ptr = ptr.successor
            ptr.successor = self.current = Node(data, None)  # Add node to last
            self.no += 1

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.successor
            self.no -= 1

    def remove_last(self):
        if self.head is not None:
            if self.head.successor is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while ptr.successor is not None:
                    pre = ptr
                    ptr = ptr.successor
                pre.successor = None  # Set the second last node to the last node
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.successor is not p:
                    ptr = ptr.successor
                    if ptr is None:
                        return  # ptr was not exist
                    ptr.successor = p.successor
                    self.current = ptr
                    self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    def next(self) -> bool:
        if self.current is None or self.current.successor is None:
            return False
        self.current = self.current.successor
        return True

    def print_current_node(self) -> None:
        if self.current is None:
            print('No current node exists!')
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next


if __name__ == '__main__':
    print('To be continued')
