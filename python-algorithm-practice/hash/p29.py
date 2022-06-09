"""
    Problem 29: Jewels and Stones

    Question: Count total number of jewels in given stone
    Source: leetcode 771 (https://leetcode.com/problems/jewels-and-stones/

"""
import collections

from common.common_function import test_result_2


# Solution 1: Using hash table
def num_jewels_in_stones_1(j: str, s: str) -> int:
    freq_s = {}
    count = 0

    for char in s:
        if char not in freq_s:
            freq_s[char] = 1
        else:
            freq_s[char] += 1

    for char in j:
        if char in freq_s:
            count += freq_s[char]

    return count


# Solution 2: Using default dictionary
def num_jewels_in_stones_2(j: str, s: str) -> int:
    freq_s = collections.defaultdict(int)
    count = 0

    for char in s:
        freq_s[char] += 1

    for char in j:
        count += freq_s[char]

    return count


# Solution 3: Using counter
def num_jewels_in_stones_3(j: str, s: str) -> int:
    freq_s = collections.Counter(s)
    count = 0

    for char in j:
        count += freq_s[char]

    return count


# Solution 4: Using pythonic method
def num_jewels_in_stones_4(j: str, s: str) -> int:
    return sum(i in j for i in s)


function_list = [num_jewels_in_stones_1, num_jewels_in_stones_2, num_jewels_in_stones_3, num_jewels_in_stones_4]


if __name__ == "__main__":
    jewels = "aA"
    stone = "aAAbbbb"
    test_result_2('String', function_list, jewels, stone)
