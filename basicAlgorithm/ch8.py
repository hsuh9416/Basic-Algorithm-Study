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

Null = -1


class Node:

    def __init__(self, data: Any = None, successor: Node = None):
        """ Initialize """
        self.data = data  # Data
        self.successor = successor  # Successor node


class NodeCursor:

    def __init__(self, data=Null, successor=Null, d_next=Null):
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


class LinkedListCursor(object):
    _instance = None

    def __init__(self, capacity: int):
        """ Initialize """
        self.head = Null  # Head node index
        self.current = Null  # Current node index
        self.max = Null  # The last record used; Current tail node index
        self.deleted = Null  # Head node index of free list
        self.capacity = capacity  # Size of the list
        self.n = [NodeCursor()] * self.capacity  # List itself
        self.no = 0

    def __new__(cls, capacity: int):  # Singleton
        if cls._instance is None:
            cls._instance = super(LinkedListCursor, cls).__new__(cls)
        return cls._instance

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        if self.deleted == Null:  # No deleted record exists
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max  # Use new record to write
            else:
                return Null
        else:
            rec = self.deleted  # Get first deleted node index
            self.deleted = self.n[rec].d_next  # Presetting next deleted head node index
            return rec  # Use free index first(rather than issuing new index number)

    def delete_index(self, idx: int):
        if self.deleted == Null:  # First deletion
            self.deleted = idx  # Insert deleted index to the head of free list
            self.n[idx].d_next = Null  # No other deleted index exists so set as 'None'
        else:
            rec = self.deleted
            self.deleted = idx  # Insert deleted index to the head of free list
            self.n[idx].d_next = rec  # Set original deleted index as next node index

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].successor
        return Null

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first(self, data: Any):
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = NodeCursor(data, ptr)
            self.no += 1

    def add_last(self, data: Any):
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].successor != Null:  # Proceed until the end
                ptr = self.n[ptr].successor
            rec = self.get_insert_index()
            if rec != Null:
                self.n[ptr].successor = self.current = rec
                self.n[rec] = NodeCursor(data)  # Add node to last
                self.no += 1

    def remove_first(self):
        if self.head != Null:
            ptr = self.n[self.head].successor
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self):
        if self.head != Null:
            if self.n[self.head].successor == Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].successor != Null:  # Proceed until the end
                    pre = ptr
                    ptr = self.n[ptr].successor
                self.n[pre].successor = Null  # Set the second last node to the last node
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int):  # Remove intended node
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].successor != p:  # Stop loop when self.n[ptr].successor == p
                    ptr = self.n[ptr].successor
                    if ptr == Null:
                        return  # ptr was not exist
                self.n[ptr].successor = Null
                self.delete_index(p)
                self.n[ptr].successor = self.n[p].successor
                self.current = ptr
                self.no -= 1

    def remove_current_node(self):
        self.remove(self.current)

    def clear(self):
        while self.head != Null:  # Proceed removing one by one
            self.remove_first()
        self.current = Null

    def next(self) -> bool:
        if self.current == Null or self.n[self.current].successor == Null:
            return False
        self.current = self.n[self.current].successor
        return True

    def print_current_node(self):
        if self.current == Null:
            print('No current node exists!')
        else:
            print(self.n[self.current].data)

    def print(self):
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].successor

    def dump(self):
        for i in self.n:
            print(f'[{i}] {i.data} {i.successor} {i.d_next}')

    def __iter__(self) -> ArrayLinkedListInterator:
        return ArrayLinkedListInterator(self.n, self.head)


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


class ArrayLinkedListInterator:

    def __init__(self, n: Any, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListInterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].successor  # Presetting before future next() call
            return data


def run_menu(lst: Any) -> None:
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


def linkedlist_cursor_test():
    lst = LinkedListCursor(100)
    run_menu(lst)


if __name__ == '__main__':
    linkedlist_test()
    linkedlist_cursor_test()
