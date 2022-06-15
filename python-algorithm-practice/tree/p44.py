"""
    Problem 44: Diameter of Binary Tree

    Question: Find the longest path passing only the same value
    Source: leetcode 687 (https://leetcode.com/problems/longest-univalue-path/

"""
from common.common_function import to_binary_tree, test_result_single, TreeNode


# Solution: Calculating path length using status value DFS
class Solution:
    result = 0

    def longest_uni_value_path(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)

        dfs(root)
        return self.result


function_list = [Solution().longest_uni_value_path]


if __name__ == "__main__":
    tree_node_list_1 = [5, 4, 5, 1, 1, 5]
    tree_node_1 = to_binary_tree(tree_node_list_1)
    print(f"Given Input Info: root = {[5, 4, 5, 1, 1, 5]}", end='\n\n')
    test_result_single(0, function_list, tree_node_1)
    print()
    tree_node_list_2 = [1, 4, 5, 4, 4, 5]
    tree_node_2 = to_binary_tree(tree_node_list_2)
    print(f"Given Input Info: root = {[1, 4, 5, 4, 4, 5]}", end='\n\n')
    test_result_single(0, function_list, tree_node_2)
