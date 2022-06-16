"""
    Problem 52: Range Sum of BST

    Question: Find a sum of nodes having value from L to R by given BST
    Source: leetcode 938 (https://leetcode.com/problems/range-sum-of-bst/

"""
from common.common_function import test_result_single, to_binary_tree, TreeNode


# Solution 1: Using brute force search as recursive structure DFS
def range_sum_bst_1(root: TreeNode, nl: int, nr: int) -> int:
    if not root:
        return 0

    result = root.val if nl <= root.val <= nr else 0
    result += range_sum_bst_1(root.left, nl, nr) + range_sum_bst_1(root.right, nl, nr)
    return result


# Solution 2: Node searching by DFS branching
def range_sum_bst_2(root: TreeNode, nl: int, nr: int) -> int:
    def dfs(sub_root: TreeNode):
        if not sub_root:
            return 0

        if sub_root.val < nl:
            return dfs(sub_root.right)
        elif sub_root.val > nr:
            return dfs(sub_root.left)

        return sub_root.val + dfs(sub_root.left) + dfs(sub_root.right)

    return dfs(root)


# Solution 3: Search node using recursive structure DFS
def range_sum_bst_3(root: TreeNode, nl: int, nr: int) -> int:
    stack, sum_num = [root], 0

    while stack:
        node = stack.pop()
        if node:
            if node.val > nl:
                stack.append(node.left)
            if node.val < nr:
                stack.append(node.right)
            if nl <= node.val <= nr:
                sum_num += node.val

    return sum_num


# Solution 4: Search node using recursive structure BFS
def range_sum_bst_4(root: TreeNode, nl: int, nr: int) -> int:
    stack, sum_num = [root], 0

    while stack:
        node = stack.pop(0)
        if node:
            if node.val > nl:
                stack.append(node.left)
            if node.val < nr:
                stack.append(node.right)
            if nl <= node.val <= nr:
                sum_num += node.val

    return sum_num


function_list = [range_sum_bst_1, range_sum_bst_2, range_sum_bst_3, range_sum_bst_4]

if __name__ == "__main__":
    tree_node_list = [10, 5, 15, 3, 7, None, 18]
    num_l = 7
    num_r = 15
    tree_node = to_binary_tree(tree_node_list)
    print(f"Given Input Info: root = {tree_node_list}, L = {num_l}, R = {num_r}", end='\n\n')
    list_len = len(function_list)
    times = [test_result_single(i, function_list, tree_node, num_l, num_r) for i in range(list_len)]

    print(f"Solution {times.index(min(times)) + 1} was the fastest!")
