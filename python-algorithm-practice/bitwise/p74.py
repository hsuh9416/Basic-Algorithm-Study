"""
    Problem 74: Number of 1 Bits

    Question: Print the number of 1 bits by given unsigned integer
    Source: leetcode 191 (https://leetcode.com/problems/number-of-1-bits/
"""
from common.common_function import test_result


# Solution 1: Count '1'
def hamming_weight_1(n: int) -> int:
    return bin(n).count('1')


# Solution 1: Bitwise operation
def hamming_weight_2(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


function_list = [hamming_weight_1, hamming_weight_2]


if __name__ == "__main__":
    data_1 = 0b0000000000000000000000000001011
    test_result('Binary String', function_list, data_1)
    print()
    data_2 = 0b0000000000000000000000010000000
    test_result('Binary String', function_list, data_2)
    print()
    data_3 = 0b11111111111111111111111111111101
    test_result('Binary String', function_list, data_3)
