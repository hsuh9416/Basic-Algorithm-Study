"""
    Ch1 Basic of Algorithm(알고리즘 기초)
    * Skipped too simple examples

    * important notes
     1) Following types of expressions are allowed:
        ex> if 10 <= x <= 90: - general mathematics expression
        ex> if not(x < 0 or x > 90): - De-Morgan law expression
    2) Python deal with data, function, class, module, package as 'Object'.
        => Therefore, Python variable do not have value.
        => Variable only acts as a name referencing its connected object.
        => Every object occupies memory, and has its own identity number.
"""

import math
import random
import pprint
# import statistics


def get_numbers():
    a, b, c = None, None, None
    while a is None:
        try:
            temp = int(input('Enter int a: ').strip())
            a = temp
        except ValueError:
            print('Enter integer number only!')
    while b is None:
        try:
            temp = int(input('Enter int b: ').strip())
            b = temp
        except ValueError:
            print('Enter integer number only!')
    while c is None:
        try:
            temp = int(input('Enter int c: ').strip())
            c = temp
        except ValueError:
            print('Enter integer number only!')
    return a, b, c


def create_random_num():
    n, start, end = None, None, None
    while n is None:
        try:
            temp = int(input('Enter numbers to be created: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    while start is None:
        try:
            temp = int(input('Enter minimum number for range: ').strip())
            if temp < 0:
                raise TypeError
            start = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    while end is None:
        try:
            temp = int(input('Enter maximum number for range: ').strip())
            if temp <= start:
                raise TypeError
            end = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then {start}!')
    return n, start, end


def simple_max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num


def simple_mid(a, b, c):
    if a >= b:
        return b if b >= c else a if a <= c else c
    else:
        return a if a > c else b if b > c else b


def get_maximum_simple():
    x, y, z = get_numbers()
    print(f'The maximum number from [{x}, {y}, {z}] is {simple_max(x, y, z)}')


def get_maximum_advanced():
    n, start, end = create_random_num()
    rand_list = [random.randint(start, end) for _ in range(n)]
    print('list created: ', end='')
    pprint.pprint(rand_list)
    rand_list.sort(reverse=True)  # dependent sorting
    max_num = rand_list[0]  # First index is maximum
    # max_num = max(rand_list)  # Via built-in function
    print(f'The maximum number from {n} numbers is {max_num}')


def get_median_simple():
    x, y, z = get_numbers()
    print(f'The median number from [{x}, {y}, {z}] is {simple_mid(x, y, z)}')


def get_median_advanced():
    n, start, end = create_random_num()
    rand_list = [random.randint(start, end) for _ in range(n)]
    print('list created: ', end='')
    pprint.pprint(rand_list)
    rand_list.sort()  # ascendant sorting

    if n % 2 == 0:  # if length of list is even
        mid_high_idx = int(n/2)
        mid_l, mid_h = rand_list[mid_high_idx-1], rand_list[mid_high_idx]
        # mid_l, mid_h = statistics.median_high(rand_list), statistics.median_low(rand_list)  # Via library function
        print(f'The median number from {n} numbers are {mid_l}, {mid_h}')
    else:
        mid_idx = math.ceil(n/2)
        mid_num = rand_list[mid_idx]
        # mid_num = statistics.median(rand_list) # Via library function
        print(f'The median number from {n} numbers is {mid_num}')


def check_id():
    print(f'set variable "k" as number "25"')
    k = 25
    print(f'id of number "25" is ={id(25)} and id of variable "k" is {id(k)}')
    print(f'Is id of number "25" and id of variable "k" are the same? "{id(25)==id(k)}"')
    print(f'id of number "35" is ={id(35)} and id of variable "k" has changed as number "35"')
    k = 35
    print(f'id of number "25" is ={id(25)} and id of variable "k" is {id(k)}')
    print(f'Is id of number "25" and id of variable "k" are the same? "{id(25) == id(k)}"')
    print('Therefore variable "k" is just a name tag for assigned object!')


if __name__ == "__main__":
    get_maximum_simple()
    get_maximum_advanced()
    get_median_simple()
    get_median_advanced()
    check_id()
