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
from typing import Any, Type


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


if __name__ == '__main__':
    print('To be continued')
