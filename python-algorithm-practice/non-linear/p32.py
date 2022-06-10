"""
    Problem 32: Number of Islands

    Question: Given a 2D grid map assuming 1 as land and 0 as water, count the number of islands
    Source: leetcode 200 (https://leetcode.com/problems/number-of-islands/
"""
from typing import List
from common.common_function import test_result


# Solution: Search graph using DFS
def num_islands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i_g in range(len(grid)):
        for j_g in range(len(grid[0])):
            if grid[i_g][j_g] == '1':
                dfs(i_g, j_g)
                count += 1

    return count


function_list = [num_islands]


if __name__ == "__main__":
    grid_map_1 = [
      ["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]
    ]
    test_result('Numbers', function_list, grid_map_1)
    print()
    grid_map_2 = [
      ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]
    ]
    test_result('List', function_list, grid_map_2)
