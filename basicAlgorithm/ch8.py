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
    2) Linked List with cursor
        => Cursor: A pointer represented by an integer index; Index of the next node
        => Cursor indicates that the back node is in the position of which presented by its index number
        => If number of data is predictable and stable, then can use cursor to avoid cost of frequent memory changing
"""
from __future__ import annotations
from typing import Any
from enum import Enum
from ch3 import select_menu

LinkedList_Menu = Enum('LinkedList_Menu',
                       ['INSERT_FIRST', 'INSERT_LAST', 'DELETE_HEAD',
                        'DELETE_TAIL', 'PRINT_CURRENT', 'MOVE_NEXT',
                        'DELETE_CURRENT', 'CLEAR_ALL', 'SEARCH', 'IS_PRESENT',
                        'PRINT_ALL', 'SCAN', 'TERMINATE'
                        ]
                       )


class Node:

    def __init__(self, data: Any = None, successor: Node = None):
        """ Initialize """
        self.data = data  # Data
        self.successor = successor  # Successor node


class NodeCursor:

    def __init__(self, data=None, successor=None, d_next=None):
        """ Initialize """
        self.data = data  # Data
        self.successor = successor  # Cursor index of the list
        self.d_next = d_next  # Cursor index of free list


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
            ptr = ptr.successor
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        ptr = self.head
        self.head = self.current = Node(data, ptr)  # Set head node to new node then link to the old head node
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
            self.head = self.current = self.head.successor  # Set Original head node to next node then store
            self.no -= 1

    def remove_last(self):
        if self.head is not None:
            if self.head.successor is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while ptr.successor is not None:  # Proceed until the end
                    pre = ptr
                    ptr = ptr.successor
                pre.successor = None  # Set the second last node to the last node
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:  # Remove intended node
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.successor is not p:  # Stop loop when ptr.successor == p
                    ptr = ptr.successor
                    if ptr is None:
                        return  # ptr was not exist
                ptr.successor = p.successor  # Make to skip p itself
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head is not None:  # Proceed removing one by one
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
            ptr = ptr.successor

    def __iter__(self) -> LinkedListInterator:
        return LinkedListInterator(self.head)


class LinkedListCursor:

    def __init__(self, capacity: int):
        """ Initialize """
        self.head = None  # Head node
        self.current = None  # Current node
        self.max = None  # Current tail recode
        self.deleted = None  # Head node of free list
        self.capacity = capacity  # Size of the list
        self.n = [Node()] * self.capacity  # List itself
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        pass


class LinkedListInterator:

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListInterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.successor  # Presetting before future next() call
            return data


def run_menu(lst: LinkedList) -> None:
    while True:
        menu = select_menu(LinkedList_Menu)

        if menu == LinkedList_Menu.INSERT_FIRST:  # Add to head node
            lst.add_first(input('Enter the value to add at head node: '))

        elif menu == LinkedList_Menu.INSERT_LAST:  # Add to tail node
            lst.add_last(input('Enter the value to add at tail node: '))

        elif menu == LinkedList_Menu.DELETE_HEAD:  # Remove current head node
            lst.remove_first()

        elif menu == LinkedList_Menu.DELETE_TAIL:  # Remove current tail node
            lst.remove_last()

        elif menu == LinkedList_Menu.PRINT_CURRENT:  # Print current node
            lst.print_current_node()

        elif menu == LinkedList_Menu.MOVE_NEXT:  # Move to the next node
            lst.next()

        elif menu == LinkedList_Menu.DELETE_CURRENT:  # Remove current node
            lst.remove_current_node()

        elif menu == LinkedList_Menu.CLEAR_ALL:  # Remove all node
            lst.clear()

        elif menu == LinkedList_Menu.SEARCH:  # Search the intended value
            pos = lst.search(input('Enter the value to search: '))
            if pos >= 0:
                print(f'The index of the data: {pos}')
            else:
                print('The data is not exists!')

        elif menu == LinkedList_Menu.IS_PRESENT:  # Check the value is present
            answer = input('Enter the value to check if present: ')
            print(f'Result: {"Exists" if answer in lst else "Not Exists"}')

        elif menu == LinkedList_Menu.PRINT_ALL:  # Show all values in the list
            lst.print()

        elif menu == LinkedList_Menu.SCAN:  # Show the data one by one
            for e in lst:
                print(e)

        else:  # End the menu
            break


def linkedlist_test():
    lst = LinkedList()
    run_menu(lst)


if __name__ == '__main__':
    linkedlist_test()
