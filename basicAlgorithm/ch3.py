"""
    Ch3 Search Algorithm(검색 알고리즘)
    * Skipped too simple examples

    * important notes
    1) linear search
        => The Only method can be used when sequence was unable to be sorted.
        => Time complexity(linear time): O(n)
        => At each iteration, two exit conditions are checked:
            a) Number of Iteration  == Length of Target List(**)
            b) The value of specific element of Target List == Target value
    2) Sentinel method
        => Adjusted linear search.
        => By add target value to target list reduce the total search cost by 1/2 (** a) condition can be ignored)
    3) Binary search
        => Sort, Divide, Search
        => Time complexity(logarithmic time): O(log n)
    4) Hash-based search
        => Easily capable for Data Search & Data insert & Data delete
        => Hash function: function that transfers key(value of element) to hash value(index of element)
        => Hash table: Table mapped the hash value as a key and the element value(bucket)
        => the key for hashing == the value of element == the value ot the hash table == bucket assigned value
        => the value of hashing == the hash value == the index of the hash table == bucket slot
        => [key:hash value = n:1] == [hash value:bucket assigned = 1:n] ---> Hash collision occurs!
    5) Solution for hash collision - Chaining
        => Chaining(Open hashing): manage values within tha same hash value by linked list
        => How search function works:
            a> Change key to hash value
            b> Find bucket having hash value as index
            c> Search the linked list in the bucket(Applies linear Search for the linked list)
            d> Success: Return the hash value
               Fail: Return None
        => How add function works:
            a> Change key to hash value
            b> Find bucket having hash value as index
            c> Search the linked list in the bucket(Applies linear Search for the linked list)
            d> Success: Add the node object to hash table and return True
               Fail: Return False
        => How delete function works:
            a> Change key to hash value
            b> Find bucket having hash value as index
            c> Search the linked list in the bucket(Applies linear Search for the linked list)
            d> Success: Delete the node object to hash table and return True
               Fail: Return False
    6) Solution for hash collision - Open address method
        => Open address method(Closed hashing: Repeat hashing(rehashing) until finding empty bucket slot for the value
        => Also called as 'Linear probing'
"""
from __future__ import annotations
from typing import Any, Sequence
from ch2 import rand_list
import hashlib
from enum import Enum


Menu = Enum('Menu',['Add','Delete','Search','Dump','Terminate'])


def seq_search(a: Sequence, key: Any) -> Any:  # Simple linear Search
    for i in range(len(a)):
        if a[i] == key:
            return i
    return None


def seq_search_advanced(a: list, key: Any) -> Any:  # Sentinel method applied
    li = a[:] + [key]  # To avoid modification!
    for i in range(len(li)):
        if li[i] == key:
            return i


def bin_search(a: Sequence, key: Any) -> Any:  # Basic binary search
    idx_s = 0  # the index of the first item
    idx_e = len(a) - 1  # the index of the last item

    while True:
        idx_m = (idx_s + idx_e) // 2  # the index of the middle item
        if a[idx_m] == key:
            return idx_m  # Success
        elif a[idx_m] < key:
            idx_s = idx_m + 1  # Search from range after the index the middle
        else:
            idx_e = idx_m - 1  # Search from range before the index the middle
        if idx_s > idx_e:
            break
    return -1  # Fail


def get_list_key():  # General function to create list and key
    li = rand_list()
    ky = None

    while ky is None:
        try:
            temp = int(input('Enter numbers to be find: ').strip())
            ky = temp
        except ValueError:
            print('Enter integer number only!')
    return li, ky


class Node:  # Node(= bucket) class to compose hashing

    def __init__(self, key: Any, value: Any, next: Node) -> None:  # Initialization
        self.key = key  # Key
        self.value = value  # Value
        self.next = next  # Referencing next Node


class ChainedHash:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity  # Size of hash table
        self.table = [None] * self.capacity  # Declare hash table(list), empty bucket assigned as 'None'

    def hash_value(self, key: Any) -> int:
        """ Calculate hash value"""
        if isinstance(key, int):  # If key was int
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity  # If key was not int

    def search(self, key: Any) -> Any:
        """ Search the hash value """
        t_hash = self.hash_value(key)
        p = self.table[t_hash]

        while p is not None:  # If the next was 'None'(no more element exists) then terminate the loop
            if p.key == key:
                return p.value  # Return the value of node
            p = p.next  # Find next node

        return None  # Search fail!

    def add(self, key: Any, value: Any) -> bool:
        """ Add the hash value to the hash table"""
        t_hash = self.hash_value(key)
        p = self.table[t_hash]

        while p is not None:  # If the next was 'None'(no more element exists) then terminate the loop
            if p.key == key:
                return False  # Fail to add
            p = p.next  # Find next node

        temp = Node(key, value, self.table[t_hash])  # Generate node object
        self.table[t_hash] = temp  # Add the node object
        return True  # Success to add

    def remove(self, key:Any) -> bool:
        """ Delete the hash value from the hash table """
        t_hash = self.hash_value(key)
        p = self.table[t_hash]  # Current Node
        pp = None  # Previous node

        while p is not None:  # If the next was 'None'(no more element exists) then terminate the loop
            if p.key == key:
                if pp is None:
                    self.table[t_hash] = p.next  # Replace current node as the next node
                else:
                    pp.next = p.next  # Make new connection skipping target hash value
                return True  # Success to delete
            pp = p  # Set current node as previous node
            p = p.next  # Set next node as current node
        return False  # Fail to delete

    def dump(self) -> None:
        """ Dump the hash table """
        for i in range(self.capacity):  # print each bucket
            p = self.table[i]
            print(i, end='')
            while p is not None:  # print linked list elements in each bucket
                print(f' -> {p.key} {p.value}', end='')
                p = p.next
            print()


def seq_search_test():  # Simple linear Search Test
    li, ky = get_list_key()
    result = seq_search(li, ky)

    if result is None:
        print(f'Number {ky} does not exists!')
    else:
        print(f'Index Number of number {ky} from the list = {result}')


def sentinel_method_test():  # sentinel method applied Test
    li, ky = get_list_key()
    result = seq_search_advanced(li, ky)

    if result == len(li):
        print(f'Number {ky} does not exists!')
    else:
        print(f'Index Number of number {ky} from the list = {result}')


def binary_search_test():  # Simple binary Search Test
    li, ky = get_list_key()
    li.sort()  # Sort the target list ascendant
    result = bin_search(li, ky)

    if result == -1:
        print(f'Number {ky} does not exists!')
    else:
        print(f'Index Number of number {ky} from the list = {result}')


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        try:
            print(*s, sep='  ', end='')
            choice = int(input(': ').strip())
            if not 1 <= choice <= len(Menu):
                raise TypeError
            return Menu(choice)
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Please enter the number from 1 to {len(Menu)}!')


def hashing_chaining_test():  # Hashing(applied chained hash) test
    hash_table = ChainedHash(13)  # Generate hash table with a capacity of 13

    while True:
        menu = select_menu()

        if menu == Menu.Add:  # Add the key, value to the hash table
            key = int(input('Enter the key to add: '))
            value = input('Enter the value to add: ')
            if not hash_table.add(key, value):
                print('Fail to add the value!')

        elif menu == Menu.Delete:  # Remove the value from the hash table
            key = int(input('Enter the key to delete: '))
            if not hash_table.remove(key):
                print('Fail to remove')

        elif menu == Menu.Search:  # Search from the hash table
            key = int(input('Enter the key to search: '))
            t = hash_table.search(key)
            if t is not None:
                print(f'The value of the key "{key}" is "{t}"')
            else:
                print(f'The value of the key "{key}" does not exist!')

        elif menu == Menu.Dump:  # Show the hash table
            hash_table.dump()

        else:
            break


if __name__ == '__main__':
    seq_search_test()
    sentinel_method_test()
    binary_search_test()
    hashing_chaining_test()