"""
    Problem 48: Balanced Binary Tree

    Question: Determine whether given binary node is height-balanced
    Source: leetcode 110 (https://leetcode.com/problems/balanced-binary-tree/

"""
from common.common_function import test_result_single, to_binary_tree, serialize, deserialize, TreeNode


# Solution: Calculate difference of height using recursive structure
def is_balanced(root: TreeNode) -> bool:
    def check(root_sub):
        if not root_sub:
            return 0

        left = check(root_sub.left)
        right = check(root_sub.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1


function_list = [is_balanced]


if __name__ == "__main__":
    tree_node_1 = to_binary_tree([3, 9, 20, None, None, 15, 7])
    tree_node_list_1 = serialize(tree_node_1)
    print(f"Given Input Info: root = {tree_node_list_1}", end='\n\n')
    test_result_single(0, function_list, tree_node_1)
    print()
    tree_node_2 = to_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    tree_node_list_2 = serialize(tree_node_2)
    print(f"Given Input Info: root = {tree_node_list_2}", end='\n\n')
    test_result_single(0, function_list, tree_node_2)
