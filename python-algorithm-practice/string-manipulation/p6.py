"""
    Problem 6. Longest Palindrome Substring

    Question: Print out the longest palindromic part from the given string
    Source: leetcode 5 (https://leetcode.com/problems/longest-palindromic-substring/

"""
import time


# Solution: Using recursion
def longest_palindrome(input_example: str) -> str:

    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(input_example) and input_example[left] == input_example[right]:
            left -= 1
            right += 1
        return input_example[left + 1:right]

    if len(input_example) < 2 or input_example == input_example[:: -1]:
        return input_example
    result = ''

    for i in range(len(input_example) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


def test_result(input_example: str) -> None:
    print(f'Given String: {input_example}')

    start_1 = time.perf_counter()
    result = longest_palindrome(input_example)
    end_1 = time.perf_counter()
    time_elapsed_1 = end_1 - start_1

    print(f'Solution Result: {result}')
    print(f'Solution Time elapsed: {time_elapsed_1}')


if __name__ == "__main__":
    input_example_1 = "babad"
    test_result(input_example_1)
    print()
    input_example_2 = "cbbd"
    test_result(input_example_2)
