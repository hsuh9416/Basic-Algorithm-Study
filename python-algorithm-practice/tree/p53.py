"""
    Problem 53: Minimum Distance Between BST Nodes

    Question: Print out the difference between the value of the smallest node and the difference between the two nodes
    Source: leetcode 783 (https://leetcode.com/problems/minimum-distance-between-bst-nodes/

"""
import sys
from common.common_function import test_result_single, to_binary_tree, TreeNode


# Solution 1: Using recursive structure, circulate as inorder
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def min_diff_in_bst_1(self, root: TreeNode) -> int:
        if root.left:
            self.min_diff_in_bst_1(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.min_diff_in_bst_1(root.right)

        return self.result


"""
# Solution 2: Using repetitive structure, circulate as inorder
def min_diff_in_bst_2(root: TreeNode) -> int:
    prev = -sys.maxsize
    result = sys.maxsize

    stack = []
    node = root

    while stack and node:
        while node:
            stack.append(node)
            node = node.left

        node.stack.pop()

        result = min(result, node.val - prev)
        prev = node.val

        node = node.right

    return result
"""

function_list = [Solution().min_diff_in_bst_1]


if __name__ == "__main__":
    list_len = len(function_list)
    tree_node_list_1 = [4, 2, 6, 1, 3, None, None]
    tree_node_1 = to_binary_tree(tree_node_list_1)
    print(f"Given Input Info: root = {tree_node_1}", end='\n\n')
    times = [test_result_single(i, function_list, tree_node_1) for i in range(list_len)]
    print(f"Solution {times.index(min(times)) + 1} was the fastest!", end="\n\n")
    tree_node_list_2 = [10, 4, 15, 1, 8, None, None]
    tree_node_2 = to_binary_tree(tree_node_list_2)
    print(f"Given Input Info: root = {tree_node_2}", end='\n\n')
    times = [test_result_single(i, function_list, tree_node_2) for i in range(list_len)]
    print(f"Solution {times.index(min(times)) + 1} was the fastest!")
