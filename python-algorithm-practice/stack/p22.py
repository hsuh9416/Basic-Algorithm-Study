"""
    Problem 22: Daily Temperatures

    Question: Print out each of the days to wait for given temperature information from list
    Source: leetcode 739 (https://leetcode.com/problems/daily-temperatures/

"""
from typing import List

from common.common_function import test_result_single


# Solution: Compare stack
def daily_temperatures(temp: List[int]) -> List[int]:
    answer = [0]*len(temp)
    stack = []
    for i, cur in enumerate(temp):
        while stack and cur > temp[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


function_list = [daily_temperatures]


if __name__ == "__main__":
    temp_list = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f'Given input Info: {temp_list}')
    test_result_single(0, function_list, temp_list)
