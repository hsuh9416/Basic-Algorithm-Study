"""
    Problem 47: Serialize and Deserialize Binary Tree

    Question: Implement a function that can serialize and deserialize a binary tree to an array

    Source: leetcode 297 (https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

"""
from common.common_function import to_binary_tree, serialize, deserialize


# Solution : Implementing serialization and deserialization
if __name__ == "__main__":
    tree_node = tree_node_list = to_binary_tree([1, 2, 3, None, None, 4, 5])
    print(f"Given Tree Node Info = {tree_node}", end='\n\n')
    serialized = serialize(tree_node)
    print(f"Serialized result = {serialized}", end='\n\n')
    deserialized = deserialize(serialized)
    print(f"Deserialized result = {deserialized}", end='\n\n')
