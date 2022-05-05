"""
    Ch3 Search Algorithm(검색 알고리즘)
    * Skipped too simple examples

    * important notes
    1) linear search
        => The Only method can be used when sequence was unable to be sorted.
        => At each iteration, two exit conditions are checked:
            a) Number of Iteration  == Length of Target List(**)
            b) The value of specific element of Target List == Target value
    2) Sentinel method
        => Adjusted linear search.
        => By add target value to target list reduce the total search cost by 1/2 (** a) condition can be ignored)
    3) Binary search

"""
from typing import Any, Sequence
from ch2 import rand_list


def seq_search(a: Sequence, key: Any) -> Any:  # Simple linear Search
    i = 0
    for i in range(len(a)):
        if a[i] == key:
            return i
    return None


def seq_search_test():  # Simple linear Search Test
    li = rand_list()
    ky = None

    while ky is None:
        try:
            temp = int(input('Enter numbers to be find: ').strip())
            ky = temp
        except ValueError:
            print('Enter integer number only!')
    result = seq_search(li, ky)

    if result is None:
        print(f'Number {ky} does not exists!')
    else:
        print(f'Index Number of number {ky} from the list = {result}')


if __name__ == '__main__':
    seq_search_test()