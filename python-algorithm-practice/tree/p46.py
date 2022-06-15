"""
    Problem 46: Diameter of Binary Tree

    Question: Merge two binary trees. Sum up the value of nodes having the same index
    Source: leetcode 617 (https://leetcode.com/problems/merge-two-binary-trees/

"""
from common.common_function import to_binary_tree, test_result_single, TreeNode


# Solution: Recursive searching
def merge_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = merge_trees(t1.left, t2.left)
        node.right = merge_trees(t1.right, t2.right)

        return node
    else:
        return t1 or t2


function_list = [merge_trees]


if __name__ == "__main__":
    tree_node_list_1 = [1, 3, 2, 5, None, None, None]
    tree_node_list_2 = [2, 1, 3, None, 4, None, 7]
    tree_node_1 = to_binary_tree(tree_node_list_1)
    tree_node_2 = to_binary_tree(tree_node_list_2)
    print(f"Given Input Info: t1 = {[1, 3, 2, 5, None, None, None]}, t2 = {[2, 1, 3, None, 4, None, 7]}", end='\n\n')
    test_result_single(0, function_list, tree_node_1, tree_node_2)
