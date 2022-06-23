"""
    Problem 69: Search a 2D Matrix II

    Question: Implement an efficient algorithm for finding values in an m x m matrix
    * The matrix is sorted in ascending order from left to right and top to bottom
    Source: leetcode 240 (https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
from typing import Any, List
from common.common_function import test_result_single


# Solution 1: Search from backward of first row
def search_matrix_1(matrix: List[List[int]], target: int) -> Any:
    if not matrix:
        return False
    row = 0
    col = len(matrix[0]) - 1

    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
    return False


# Solution 2: Using pythonic method
def search_matrix_2(matrix: List[List[int]], target: int) -> Any:
    return any(target in row for row in matrix)


function_list = [search_matrix_1, search_matrix_2]


if __name__ == "__main__":
    lg = len(function_list)
    number_list = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
    target_num = 5
    print(f"Given Input Info: numbers = {number_list}, target = {target_num}", end='\n\n')
    result_lists = [test_result_single(i, function_list, number_list, target_num) for i in range(lg)]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
    print()
    target_num = 20
    print(f"Given Input Info: numbers = {number_list}, target = {target_num}", end='\n\n')
    result_lists = [test_result_single(i, function_list, number_list, target_num) for i in range(lg)]
    print(f"Solution {result_lists.index(min(result_lists)) + 1} was the fastest!")
