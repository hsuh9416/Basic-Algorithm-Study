"""
    Problem 62: Valid Anagram

    Question: Determine if t is an anagram of s
    Source: leetcode 242 (https://leetcode.com/problems/valid-anagram/

"""
from common.common_function import test_result_single


# Solution: Comparison using sort
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


function_list = [is_anagram]


if __name__ == "__main__":
    s_1 = "anagram"
    t_1 = "nagaram"
    print(f"Given Input Info: s = {s_1}, t = {t_1}", end='\n\n')
    test_result_single(0, function_list, s_1, t_1)
    print()
    s_2 = "rat"
    t_2 = "car"
    print(f"Given Input Info: s = {s_2}, t = {t_2}", end='\n\n')
    test_result_single(0, function_list, s_2, t_2)
