"""
    Problem 72: Sum of Two Integers

    Question: Find the sum of two integers a and b
    * The + or - operator cannot be used
    Source: leetcode 461 (https://leetcode.com/problems/sum-of-two-integers/
"""
from common.common_function import test_result_2


# Solution 1: Full adder implementation
def get_sum_1(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)

    result = []
    carry = 0
    sum_1 = 0
    for i in range(32):
        A = int(a_bin[31 - i])
        B = int(b_bin[31 - i])

        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum_1 = carry ^ Q2
        carry = Q1 | Q3

        result.append(str(sum_1))

    if carry == 1:
        result.append('1')

    result = int(''.join(result[::-1]), 2) & MASK

    if result > INT_MAX:
        result = ~(result ^ MASK)

    return result


# Solution 2: Full adder implementation - Simpler
def get_sum_2(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a > INT_MAX:
        a = ~(a ^ MASK)
    return a


function_list = [get_sum_1, get_sum_2]


if __name__ == "__main__":
    a_num_1 = 1
    b_num_1 = 2
    test_result_2('Numbers', function_list, a_num_1, b_num_1)
    print()
    a_num_2 = -2
    b_num_2 = 3
    test_result_2('Numbers', function_list, a_num_2, b_num_2)