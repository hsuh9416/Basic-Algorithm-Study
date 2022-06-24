"""
    Problem 73: UTF-8 Validation

    Question: Determination based on first byte
    Source: leetcode 393 (https://leetcode.com/problems/utf-8-validation/
"""
from typing import List
from common.common_function import test_result


# Solution 1: Full adder implementation
def valid_utf8(data: List[int]) -> bool:
    def check(size):
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    start = 0

    while start < len(data):
        first = data[start]
        if (first >> 3) == 0b11110 and check(3):
            start += 4
        elif (first >> 4) == 0b1110 and check(2):
            start += 3
        elif (first >> 5) == 0b110 and check(1):
            start += 2
        elif (first >> 7) == 0:
            start += 1
        else:
            return False
    return True


function_list = [valid_utf8]


if __name__ == "__main__":
    data_1 = [197, 130, 1]
    test_result('Number List', function_list, data_1)
    print()
    data_2 = [235, 140, 4]
    test_result('Number List', function_list, data_2)