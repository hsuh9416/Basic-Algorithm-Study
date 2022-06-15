"""
    Problem 47: Serialize and Deserialize Binary Tree

    Question: Implement a function that can serialize and deserialize a binary tree to an array

    Source: leetcode 297 (https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

"""
import collections
from typing import Any
from common.common_function import to_binary_tree, TreeNode


# Solution : Implementing serialization and deserialization
def serialize(root: TreeNode) -> str:
    queue = collections.deque([root])
    result = ['#']
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)

            result.append(str(node.val))
        else:
            result.append('#')
    return ' '.join(result)


def deserialize(data: str) -> Any:
    if data == '# #':
        return None

    nodes = data.split()

    root = TreeNode(int(nodes[1]))
    queue = collections.deque([root])
    index = 2
    while queue:
        node = queue.popleft()
        if nodes[index] != '#':
            node.left = TreeNode(int(nodes[index]))
            queue.append(node.left)

        index += 1

        if nodes[index] != '#':
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)

        index += 1

    return root


if __name__ == "__main__":
    tree_node = tree_node_list = to_binary_tree([1, 2, 3, None, None, 4, 5])
    print(f"Given Tree Node Info = {tree_node}", end='\n\n')
    serialized = serialize(tree_node)
    print(f"Serialized result = {serialized}", end='\n\n')
    deserialized = deserialize(serialized)
    print(f"Deserialized result = {deserialized}", end='\n\n')
