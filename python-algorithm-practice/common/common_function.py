import time
from typing import Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        tree_node = pre_node = self
        object_print = '['
        right_flag = False
        while True:
            object_print += f"{tree_node.val}"
            if right_flag:
                if tree_node.left is None:
                    break
                else:
                    object_print += f", null, null, "
            else:
                object_print += f", "
            if tree_node.left is not None:
                pre_node = tree_node
                tree_node = tree_node.left
                right_flag = False
            else:
                if pre_node.right is not None:
                    tree_node = pre_node.right
                    right_flag = True
        return object_print + ']'

    def __str__(self) -> str:
        return str(self.val)


def to_binary_tree(items: list[int]) -> Any:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> Any:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


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
        """ Todo: Should make more reasonable result!"""
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


def test_result_single(idx: int, func_list: Any, *args) -> float:
    start = time.perf_counter()
    result = func_list[idx](*args)
    end = time.perf_counter()
    time_elapsed = end - start
    if result.__class__.__name__ == 'TreeNode':
        print(f'Solution {idx + 1} Result: {repr(result)}')
    else:
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

    print()

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
