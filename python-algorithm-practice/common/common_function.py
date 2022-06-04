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


def create_linked_list(head: list, idx=-1) -> Any:

    if idx == len(head) - 1:
        return None
    else:
        return ListNode(head[idx + 1], create_linked_list(head, idx + 1))


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