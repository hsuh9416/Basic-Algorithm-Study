"""
    Problem 71: Hamming Distance

    Question: Take two integers and count how many bits are different
    Source: leetcode 461 (https://leetcode.com/problems/hamming-distance/
"""
from common.common_function import test_result_single


# Solution: Solving XOR
def hamming_distance(x: int, y: int) -> int:
    return bin(x ^ y).count('1')


function_list = [hamming_distance]


if __name__ == "__main__":
    x_num = 1
    y_num = 4
    print(f"Given Input Info: x = {x_num}, y = {y_num}", end='\n\n')
    test_result_single(0, function_list, x_num, y_num)
