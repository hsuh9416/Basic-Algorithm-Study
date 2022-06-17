"""
    Problem 54: Construct Binary Tree from Preorder and Inorder Traversal

    Question: Build a binary tree by taking the tree's prefix and median traversal results as input
    Source: leetcode 105 (https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

"""
from typing import Any, List
from common.common_function import test_result_single, TreeNode


# Solution: Inorder traversal divide-and-conquer with preorder traversal results
def build_tree(preorder: List[int], inorder: List[int]) -> Any:
    if inorder:
        index = inorder.index(preorder.pop(0))

        node = TreeNode(inorder[index])
        node.left = build_tree(preorder, inorder[0:index])
        node.right = build_tree(preorder, inorder[index + 1:])

        return node
    else:
        return None


function_list = [build_tree]


if __name__ == "__main__":
    preorder_tree_node_list = [3, 9, 20, 15, 7]
    inorder_tree_node_list = [9, 3, 15, 20, 7]
    print(f"Given Input Info: preorder = {preorder_tree_node_list}, inorder= {inorder_tree_node_list}", end='\n\n')
    test_result_single(0, function_list, preorder_tree_node_list, inorder_tree_node_list)