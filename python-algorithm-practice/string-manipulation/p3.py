"""
    Problem 3. Reorder data in log files

    Question: Reorder data in log files
    Directions:
        1> The headers of each log are identifiers
        2> The literally consisted log comes first (rather than the numerically consisted logs)
        3> Identifiers do not affect to order but if letters of each log are identical then consider identifiers as well
        4> The numbers should be placed as its input order
    Source: leetcode 937 (https://leetcode.com/problems/reorder-data-in-log-files/

"""
from typing import List


# Solution: Using lambda and + operator
def reorder_logfiles(logs: List[str]) -> List[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


def test_result(logs_input: List[str]) -> None:
    import time
    start_1 = time.perf_counter()
    result = reorder_logfiles(logs_input)
    end_1 = time.perf_counter()
    time_elapsed_1 = end_1 - start_1

    print(f'Solution Result: {result}')
    print(f'Solution Time elapsed: {time_elapsed_1}')


if __name__ == "__main__":
    input_example = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
    test_result(input_example)
    print()
