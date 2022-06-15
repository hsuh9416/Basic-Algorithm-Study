"""
    Problem 45: Invert Binary Tree

    Question: Invert given binary tree from left to right
    Source: leetcode 226 (https://leetcode.com/problems/invert-binary-tree/

"""
import collections
from typing import Any
from common.common_function import to_binary_tree, test_result_single, TreeNode


# Solution 1: Using pythonic method
def invert_tree_1(root: TreeNode) -> Any:
    if root:
        root.left, root.right = invert_tree_1(root.right), invert_tree_1(root.left)
        return root
    return None


# Solution 2: Using repetitive structure BFS
def invert_tree_2(root: TreeNode) -> Any:
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

        return root


# Solution 3: Using repetitive structure DFS
def invert_tree_3(root: TreeNode) -> Any:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

        return root


# Solution 4: Using repetitive structure backward DFS
def invert_tree_4(root: TreeNode) -> Any:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left

        return root


function_list = [invert_tree_1, invert_tree_2, invert_tree_3, invert_tree_4]


if __name__ == "__main__":
    tree_node_list = [4, 2, 7, 1, 3, 6, 9]
    tree_node = to_binary_tree(tree_node_list)
    print(f"Given Input Info: root = {[4, 2, 7, 1, 3, 6, 9]}", end='\n\n')
    result_list = [test_result_single(i, function_list, tree_node) for i in range(len(function_list))]
    print(f"Solution {result_list.index(min(result_list)) + 1} was the fastest!")
