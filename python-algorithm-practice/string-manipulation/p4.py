"""
    Problem 4. Most Common Word

    Question: Find the most common word except banned word.
    Source: leetcode 819 (https://leetcode.com/problems/most-common-word/

"""

from typing import List
import time
import re
from collections import Counter


# Solution: Using list comprehension, Counter object
def most_common_word(par: str, ban: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', par).lower().split() if word not in ban]

    counts = Counter(words)

    return counts.most_common(1)[0][0]


def test_result(par: str, ban: List[str]) -> None:
    start_1 = time.perf_counter()
    result = most_common_word(par, ban)
    end_1 = time.perf_counter()
    time_elapsed_1 = end_1 - start_1

    print(f'Solution Result: {result}')
    print(f'Solution Time elapsed: {time_elapsed_1}')


if __name__ == "__main__":
    paragraph = 'Bob hit a ball, the hit Ball flew far after it was hit.'
    banned = ["hit"]
    test_result(paragraph, banned)
