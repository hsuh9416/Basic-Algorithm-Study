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
        => a> Find min element b> Switch with element in intended position of min element c> Repeat
    6> Straight insertion sort
        => a> Compare selected element with pre-ordered elements b> Insert the element into right position c> Repeat
    7> Shell sort: Advanced straight insertion sort
        => Sorting by group and merge after completion
        => Advanced straight insertion sorting method to reduce cost of switching
        => Each dividing number should not be multiple number of each other
           (Elements of group should be mixed up properly even grouping, so to gain effect of sorting)
    8> Quick sort: The generally used prompt sorting method
        => Enable to implement recursive algorithm because quick sort is divide-and-conquer algorithm
        => a> Use a pivot element to divide two group
           b> Scan from each ends to pivot element to find out:
                From left: Search elements bigger than pivot element
                From right: Search elements smaller than pivot element
           c> Switch the two correspondent elements that found from the scan from b>
           d> End b> ~ c> when scanning ends reached to pivot element
           e> Repeat a> ~ d> until no range to be divided
        => Stack size for quick sort: log n
        => Executing quick sort when using stack:
           * Because it will be faster enough to empty stack, execute the smaller range first
            (In order to avoid simultaneously stacking too much)
        => Pivot element selection: Critical for quick sorting efficiency
           * In general, the median value will be ideal but hard to find before sorting
           * Method 1: if len(array) >= 3, then randomly choose 3 element and pick the median among them
           * Method 2: a> Sort array[0], array[(len(array) -1) // 2], array[len(array) -1]
                       b> Switch the median element with array[len(array)-2]
                       c> Choose pivot element as array[len(array)-2]
                       d> Set pl = left + 1, pr = right - 2 (Excludes already sorted 3 elements)
        => Complexity of quick sort = O(n log n) ~ O(n^2) [Worst]
        => If number of elements is not big enough, quick sort algorithm has low efficiency
    9> Built-in function 'sorted()'
        => Not in-placing array directly but returning new list of sorted elements
        => Therefore, this function also capable to immutable sequences ex> tuple


"""
from typing import MutableSequence
from random import sample
from bisect import insort
from ch4 import Stack


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


def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]  # Moving forward
            j -= 1
        a[j] = tmp  # Placing on the target position


def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0  # Starting index
        pr = i - 1  # Ending index

        while True:
            pc = (pl + pr) // 2  # Middle index from the search range

            if a[pc] == key:  # Stop searching
                break
            elif a[pc] < key:  # Only to search from backward side
                pl = pc + 1
            else:  # Only to search from forward side
                pr = pc - 1
            if pl > pr:  # Search end
                break

        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]  # Changing forwardly
        a[pd] = key  # Placing at the target position


def binary_insertion_sort2(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        insort(a, a.pop(i), 0, i)


def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
                a[j + h] = tmp
        h //= 3


def qsort_recursive(a: MutableSequence, left: int, right: int) -> None:
    n = len(a)
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:  # Re-divide and re-conquer
        qsort_recursive(a, left, pr)
    if pl < right:  # Re-divide and re-conquer
        qsort_recursive(a, pl, right)


def qsort_non_recursive(a: MutableSequence, left: int, right: int) -> None:
    range_s = Stack(right - left + 1)

    range_s.push((left, right))

    while not range_s.is_empty():  # Until ranges to divide exist
        pl, pr = left, right = range_s.pop()
        x = a[(left + right) // 2]

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr:
            range_s.push((left, pr))
        if pl < right:
            range_s.push((pl, right))


def quick_sort(a: MutableSequence):
    # qsort_recursive(a, 0, len(a) - 1)
    qsort_non_recursive(a, 0, len(a) - 1)


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
    # selection_sort(x)
    # insertion_sort(x)
    # binary_insertion_sort(x)
    # binary_insertion_sort2(x)
    # shell_sort(x)
    quick_sort(x)
    print('Array sorted: ', x)


if __name__ == '__main__':
    sort_test()
