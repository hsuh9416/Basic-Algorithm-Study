import time
from typing import Any


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


class ListNode2:
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        linked_list = self
        object_print = '['
        while True:
            object_print += f'({linked_list.key}":{linked_list.val})'
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


def linkedlist_to_list(node: ListNode) -> list:
    result_list = []
    while True:
        result_list.append(node.val)
        if node.next_node is None:
            break
        node = node.next_node

    return result_list


def test_function(func_name: str, func_obj: Any, *arg_val) -> None:
    if len(arg_val) != 0:
        print(f'Given input Info: {arg_val}')
    start = time.perf_counter()
    result = func_obj(*arg_val)
    end = time.perf_counter()
    time_elapsed = end - start
    print(f'Function {func_name} Result: {result}') if result is not None else print(f'Function {func_name} completed!')
    print(f'Function {func_name}  Time elapsed: {time_elapsed}', end='\n\n')


def test_result_single(idx: int, func_list: Any, arg_val_1: Any, arg_val_2=None) -> float:
    if arg_val_2 is None:
        start = time.perf_counter()
        result = func_list[idx](arg_val_1)
        end = time.perf_counter()
        time_elapsed = end - start
    else:
        start = time.perf_counter()
        result = func_list[idx](arg_val_1, arg_val_2)
        end = time.perf_counter()
        time_elapsed = end - start

    print(f'Solution {idx + 1} Result: {result}')
    print(f'Solution {idx + 1}  Time elapsed: {time_elapsed}', end='\n\n')

    return time_elapsed


def test_result(arg_type: str, func_list: Any, arg_val: Any) -> None:
    print(f'Given {arg_type} Info: {arg_val}')
    result_time = []
    for i in range(len(func_list)):
        print()

        start = time.perf_counter()
        result = func_list[i](arg_val)
        end = time.perf_counter()
        time_elapsed = end - start

        print(f'Solution {i + 1} Result: {result}')
        print(f'Solution {i + 1}  Time elapsed: {time_elapsed}')

        result_time.append(time_elapsed)

    if len(func_list) > 1:
        print(f"Solution {result_time.index(min(result_time)) + 1} was the fastest!")


def test_result_2(arg_type: str, func_list: Any, arg_val_1: Any, arg_val_2: Any) -> None:
    print(f'Given {arg_type} Info: {arg_val_1}, {arg_val_2}', end='\n\n')

    min_time = [0, 99999]
    for i in range(len(func_list)):

        start = time.perf_counter()
        result = func_list[i](arg_val_1, arg_val_2)
        end = time.perf_counter()
        time_elapsed = end - start

        print(f'Solution {i + 1} Result: {result}')
        print(f'Solution {i + 1}  Time elapsed: {time_elapsed}', end='\n\n')

        min_time = [i + 1, time_elapsed] if time_elapsed < min_time[1] else min_time

    if len(func_list) > 1:
        print(f"Solution {min_time[0]} was the fastest!")
