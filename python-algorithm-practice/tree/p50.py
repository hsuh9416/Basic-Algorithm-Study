"""
    Problem 50: Convert Sorted Array to Binary Search Tree

    Question: Convert an ascending sorted array into a height balanced binary search tree
    Source: leetcode 108 (https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

"""
from typing import Any, List
from common.common_function import test_result_single, TreeNode


# Solution: Constructing tree using binary searching
def sorted_array_to_bst(nums: List[int]) -> Any:
    if not nums:
        return None

    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sorted_array_to_bst(nums[:mid])
    node.right = sorted_array_to_bst(nums[mid + 1:])

    return node


function_list = [sorted_array_to_bst]


if __name__ == "__main__":
    num_list = [-10, -3, 0, 5, 9]
    print(f"Given Input Info: nums = {num_list}", end='\n\n')
    test_result_single(0, function_list, num_list)
