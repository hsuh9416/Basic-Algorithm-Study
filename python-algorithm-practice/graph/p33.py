"""
    Problem 33: Letter Combinations of a Phone Number

    Question: From given a number from 2 to 9, print all the numbers that can be combined into a phone number
    Source: leetcode 17 (https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
from typing import List
from common.common_function import test_result


# Solution: Search all combinations
def letter_combinations(digits: str) -> List[str]:
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    if not digits:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    result = []
    dfs(0, "")

    return result


function_list = [letter_combinations]


if __name__ == "__main__":
    input_str = "23"
    test_result('String Number', function_list, input_str)
