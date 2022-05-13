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
    4) Shaker sort: Advanced bubble sort, Bidirectional bubble sort, Cocktail sort, Cocktail shaker sort
    5) Straight selection sort
        => a) Find min element b) Switch with element in intended position of min element x) Repeat 
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


def bubble_sort_adv(a: MutableSequence) -> None:
    compare_count = 0  # Count number of comparison
    switch_count = 0  # Count number of switching
    n = len(a)
    k = 0
    i = 0
    while k < n - 1:  # limiting scan range when previous order has been done
        print(f'pass number = {i + 1}')
        i += 1
        last = n - 1
        for j in range(n - 1, k, -1):  # Exchanging
            for o in range(0, n - 1):
                print(f'{a[o]:2}' + (' ' if o != j - 1 else '+' if a[j - 1] > a[j] else '-'), end='')
            print(f'{a[n - 1]:2}')
            compare_count += 1
            if a[j - 1] > a[j]:
                switch_count += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
        for o in range(0, n - 1):
            print(f'{a[o]:2}', end=' ')
        print(f'{a[n - 1]:2} <= pass {i} end')
    print(f'The number of comparison = {compare_count}')
    print(f'The number of switching = {switch_count}')


def shaker_sort(a: MutableSequence) -> None:
    compare_count = 0  # Count number of comparison
    switch_count = 0  # Count number of switching
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'pass number = {i + 1}')
        i += 1
        for j in range(right, left, -1):  # Right -> Left
            for o in range(0, n - 1):
                print(f'{a[o]:2}' + (' ' if o != j - 1 else '+' if a[j - 1] > a[j] else '-'), end='')
            print(f'{a[n - 1]:2}')
            compare_count += 1
            if a[j - 1] > a[j]:
                switch_count += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        for o in range(0, n - 1):
            print(f'{a[o]:2}', end=' ')
        print(f'{a[n - 1]:2} <= pass(from right) {i} end')

        if left == right:
            break

        for j in range(left, right):  # Left -> Right
            for o in range(0, n - 1):
                print(f'{a[o]:2}' + (' ' if o != j else '+' if a[j] > a[j + 1] else '-'), end='')
            print(f'{a[n - 1]:2}')
            compare_count += 1
            if a[j] > a[j + 1]:
                switch_count += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        for o in range(0, n - 1):
            print(f'{a[o]:2}', end=' ')
        print(f'{a[n - 1]:2} <= pass(from left) {i} end')
    print(f'The number of comparison = {compare_count}')
    print(f'The number of switching = {switch_count}')


def arg_min(a: MutableSequence, start_idx: int, end_idx: int) -> int:
    min_idx = start_idx - 1
    for i in range(start_idx + 1, end_idx):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx


def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        min_idx = arg_min(a, i + 1, n)
        a[i], a[min_idx] = a[min_idx], a[i]


def sort_test():
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
    # bubble_sort(x)
    # bubble_sort_adv(x)
    # shaker_sort(x)
    selection_sort(x)
    print('Array sorted: ', x)


if __name__ == '__main__':
    sort_test()
