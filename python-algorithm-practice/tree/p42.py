"""
    Problem 42: Maximum Depth of Binary Tree

    Question: Calculate maximum depth of given binary tree
    Source: leetcode 104 (https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
import collections
from common.common_function import to_binary_tree, test_result_single, TreeNode


# Solution: Using repetitive structure
def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    return depth


function_list = [max_depth]


if __name__ == "__main__":
    tree_node_list = [3, 9, 20, None, None, 15, 7]
    tree_node = to_binary_tree(tree_node_list)
    print(f"Given Input Info: root = {repr(tree_node)}", end='\n\n')
    test_result_single(0, function_list, tree_node)
