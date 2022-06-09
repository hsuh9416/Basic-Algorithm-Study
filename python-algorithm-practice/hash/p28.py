"""
    Problem 28: Design HashMap

    Question: Design a hashmap that applies following function
    * following function list:
        put(key, value), get(key), remove(key)
    Source: leetcode 706 (https://leetcode.com/problems/design-hashmap/

"""
import collections
from common.common_function import test_function, ListNode2


# Solution: Using separate chaining
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode2)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode2(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next_node is None:
                break
            p = p.next_node
        p.next = ListNode2(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next_node
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode2() if p.next_node is None else p.next_node
            return
        prev = p
        while p:
            if p.key == key:
                prev.next_node = p.next_node
                return
            prev, p = p, p.next_node


if __name__ == "__main__":
    hashMap = MyHashMap()
    test_function('put', hashMap.put, 1, 1)
    test_function('put', hashMap.put, 2, 2)
    test_function('get', hashMap.get, 1)
    test_function('get', hashMap.get, 3)
    test_function('put', hashMap.put, 2, 1)
    test_function('get', hashMap.get, 2)
    test_function('remove', hashMap.remove, 2)
    test_function('get', hashMap.get, 2)
