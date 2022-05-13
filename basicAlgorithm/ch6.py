"""
    Ch6 Sorting Algorithm(정렬 알고리즘)
    * Skipped too simple examples

    * important notes
    1) Internal sort: Sorting method used when all data are enough to be stored in one sequence
       External sort: Sorting method used when all data are too much to be stored within one sequence
    2) Basic of sorting algorithm: Exchange, Selection, Insertion
    3) Bubble sort: Straight exchanging sort
        => The sorting method that executes by exchanging neighbored elements by comparing their size or order
        => pass: The process of exchanging neighbored elements by comparison
"""
from typing import MutableSequence
from random import sample


def bubble_sort(a: MutableSequence) -> None:
    compare_count = 0  # Count number of comparison
    switch_count = 0  # Count number of switching
    n = len(a)
    for i in range(n - 1):  # Each pass
        exchange_count = 0  # Count number of exchanging
        print(f'pass number = {i + 1}')
        for j in range(n - 1, i, -1):  # Exchanging
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + (' ' if m != j - 1 else '+' if a[j - 1] > a[j] else '-'), end='')
            print(f'{a[n - 1]:2}')
            compare_count += 1
            if a[j - 1] > a[j]:
                switch_count += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                exchange_count += 1
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end=' ')
        print(f'{a[n - 1]:2} <= pass {i + 1} end')
        if exchange_count == 0:  # No more sorting needed
            break
    print(f'The number of comparison = {compare_count}')
    print(f'The number of switching = {switch_count}')


def bubble_sort_test():
    print('Start bubble sorting')
    n = None
    while n is None:
        try:
            temp = int(input('Enter the length of array: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    x = sample(range(1, 100), n)
    print('Unsorted: ', x)
    bubble_sort(x)
    print('Bubble sorted: ', x)


if __name__ == '__main__':
    bubble_sort_test()
