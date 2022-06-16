"""
    Problem 51: Binary Search Tree to Greater Sum Tree

    Question: Make each node in BST the sum of all nodes with a value greater than the current value
    Source: leetcode 1038 (https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

"""
from common.common_function import test_result_single, to_binary_tree, TreeNode


# Solution: Accumulate node values by inorder traversal
class Solution:
    val = 0

    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bst_to_gst(root.right)
            self.val += root.val
            root.val = self.val
            self.bst_to_gst(root.left)

        return root


function_list = [Solution().bst_to_gst]


if __name__ == "__main__":
    tree_node_list = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    tree_node = to_binary_tree(tree_node_list)
    print(f"Given Input Info: nums = {tree_node_list}", end='\n\n')
    test_result_single(0, function_list, tree_node)
