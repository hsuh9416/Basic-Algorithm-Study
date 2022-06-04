import time
from typing import Any


def test_result(arg_type: str, func_list: Any, arg_val: Any) -> None:
    print(f'Given {arg_type} Info: {arg_val}')
    result_time = []
    for i in range(len(func_list)):
        print()

        start = time.perf_counter()
        result = func_list[i](arg_val)
        end = time.perf_counter()
        time_elapsed = end - start

        print(f'Solution {i + 1} Result: {result}')
        print(f'Solution {i + 1}  Time elapsed: {time_elapsed}')

        result_time.append(time_elapsed)

    if len(func_list) > 1:
        print(f"Solution {result_time.index(min(result_time)) + 1} was the fastest!")