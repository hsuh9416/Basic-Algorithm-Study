"""
    Problem 20: Valid Parentheses

    Question: Check if the parenthesized input is correct
    Source: leetcode 20 (https://leetcode.com/problems/valid-parentheses/

"""
from common.common_function import test_result_single


# Solution: Check stack equivalence
def is_valid(s: str) -> bool:
    stack = []
    table = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0


function_list = [is_valid]


if __name__ == "__main__":
    sample_input = '()[]{}'
    print(f'Given input Info: {sample_input}')
    test_result_single(0, function_list, sample_input)
