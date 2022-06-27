"""
    Problem 80: Task Scheduler
    Question: Return the least number of units of times that the CPU will take to finish all the given tasks
    Source: leetcode 621 (https://leetcode.com/problems/task-scheduler/
"""
import collections
from typing import List
from common.common_function import test_result_single


# Solution: Using queue
def lease_interval(tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            counter += collections.Counter()

        if not counter:
            break

        result += n - sub_count + 1

    return result


function_list = [lease_interval]


if __name__ == "__main__":
    task_list = ["A", "A", "A", "B", "B", "B"]
    num_n = 2
    print(f"Given Input Info: tasks = {task_list}, n = {num_n}", end='\n\n')
    test_result_single(0, function_list, task_list, num_n)
