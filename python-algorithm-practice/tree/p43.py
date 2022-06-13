"""
    Problem 43: Diameter of Binary Tree

    Question: Print the length of the longest path between two nodes in a given binary tree
    Source: leetcode 543 (https://leetcode.com/problems/diameter-of-binary-tree/

"""
from common.common_function import to_binary_tree, test_result_single, TreeNode


# Solution: Using Cumulative state value tree DFS
class Solution:
    longest = 0

    def diameter_of_binary_tree(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest


function_list = [Solution().diameter_of_binary_tree]


if __name__ == "__main__":
    tree_node_list = [1, 2, 3, 4, 5]
    tree_node = to_binary_tree(tree_node_list)
    print(f"Given Input Info: root = {[1, 2, 3, 4, 5]}", end='\n\n')
    test_result_single(0, function_list, tree_node)
