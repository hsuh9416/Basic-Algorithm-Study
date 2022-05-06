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
        => Solution for hash collision
            a> Chaining(Open hashing): manage values within tha same hash value by linked list
            b> Open address method: Repeat hashing until finding empty bucket slot for the value

"""
from __future__ import annotations
from typing import Any, Sequence, Type
from ch2 import rand_list
import hashlib


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
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity


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


if __name__ == '__main__':
    # seq_search_test()
    # sentinel_method_test()
    binary_search_test()