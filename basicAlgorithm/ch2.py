"""
    Ch1 Basic of Data Structure and Sequences(기본 자료구조와 배열)
    * Skipped too simple examples

    * important notes
    1) Comparing logics of array is allowed.
        => check the function 'compare_lists'
    2) List and Tuple computations
        => check the function 'sequence_computing'
    3) Library typing(https://docs.python.org/3/library/typing.html) - Support for type hints
        a) Any: any data type can be implemented
            => Even if sequence has various types of elements, function works!
            => Check function 'find_maximum' in which list having either float and int data types
        b) Sequence: sequence data type will be implemented
            => Including List, Tuple, Set, Etc.
            => To be specified, use ('List', 'Tuple', 'Set', Etc.) instead of 'Sequence'
    4) Function annotation in Python
        reference =>https://code.tutsplus.com/tutorials/python-3-function-annotations--cms-25689
    5) Beginning of function's execution, parameter would reference the same object as real argument.
        a) If argument was immutable: New object having identical value would be created and function updates to
           reference the new one. So real argument would not be affected from function's modification.
        b) If argument was mutable: Function updates the object of argument itself while execution. So the argument
           would be changed if function modified the value of the argument.
        c) This is called: Call by object reference
    6) Since variable only acts as a name referencing its connected object, sequence does not need to determine their
       type of element in advance.
    7) Shallow copy VS Deep copy
        a) Sallow copy: Method that copies only the value of its referencing object
        b) Deep copy: Method that copies the object itself

"""
from typing import Any, Sequence, List
from ch1 import create_random_num
from random import randint, uniform
from pprint import pprint
from copy import deepcopy

def compare_lists():
    list1 = [1, 2, 3]

    list2 = [1, 2, 3]  # identical
    print(f'{list1} == {list2} ? {list1 == list2}')

    list2 = [1, 3, 2]  # different order
    print(f'{list1} == {list2} ? {list1 == list2}')

    list2 = [2, 1, 3]  # different order, determine which is the bigger
    print(f'{list1} > {list2} ? {list1 > list2}')
    print(f'{list1} < {list2} ? {list1 < list2}')

    list2 = [1, 3, 2]  # different order2, determine which is the bigger
    print(f'{list1} > {list2} ? {list1 > list2}')
    print(f'{list1} < {list2} ? {list1 < list2}')

    list3 = [1, 2, 3, 0]  # identical, but add just one element
    print(f'{list1} == {list3} ? {list1 == list3}')
    print(f'{list1} > {list3} ? {list1 > list3}')
    print(f'{list1} < {list3} ? {list1 < list3}')

    list3 = [0, 0, 0, 0]  # compare arrays having different elements and length
    print(f'{list1} > {list3} ? {list1 > list3}')
    print(f'{list1} < {list3} ? {list1 < list3}')

    list3 = [0, 4, 0, 0]  # compare arrays having different elements and length
    print(f'{list1} > {list3} ? {list1 > list3}')
    print(f'{list1} < {list3} ? {list1 < list3}')

    list3 = [1, 4, 0, 0]  # compare arrays having different elements and length2
    print(f'{list1} > {list3} ? {list1 > list3}')
    print(f'{list1} < {list3} ? {list1 < list3}')


def sequence_computing():
    list1 = [1, 2, 3, 4]
    tuple1 = (1, 2, 3, 4)
    print(f'list= {list1}, tuple= {tuple1}')

    # using +=
    list1 += [5]
    tuple1 += (5, 6)
    print(f'list= {list1}, tuple= {tuple1}')

    # using *=
    list1 *= 2
    tuple1 *= 2
    print(f'list= {list1}, tuple= {tuple1}')

    # using slicing
    list2 = list1[2:5]
    tuple2 = tuple1[2:5]
    print(f'list= {list2}, tuple= {tuple2}')

    # use as key of dictionary(only tuple)
    dict1 = {tuple2: "Hello"}
    print(f'tuple={tuple2}, dict= {dict1}')


def rand_list() -> List:  # Arrow to give hint of return type
    n, start, end = create_random_num()
    li = list()
    for _ in range(n):
        if _ % 2 == 0:  # Even index element to be int
            li.append(randint(start, end))
        else:  # Odd index element to be float
            li.append(uniform(start, end))
    return li


def max_of(x: Sequence) -> Any:  # Arrow to give hint of return type
    """
    Function returns maximum value from given sequence
    :param x: Sequence data type object
    :return: Arbitrary data type object
    """
    maximum = x[0]
    for i in range(1, len(x)):
        if x[i] > maximum:
            maximum = x[i]
    return maximum


def find_maximum():
    print("Find maximum value of sequence X")

    seq_list = rand_list()
    print('Sequence(list) created: ')
    pprint(seq_list)
    maximum = max_of(seq_list)

    print(f"The maximum value of sequence X is {maximum}")


def func_test(extra: 'nothing to do it!', a: int, b: 'default value to be "Hello, World"' = 'Hello, World') -> float:
    print(extra, type(extra))
    print(a, type(a))
    print(b)
    return 3.5 if type(a) == int else "It's not a float!"


def annotation_test():
    x = "This is not a int!"
    y = "Hello, Python!"
    z1 = func_test('This is String', x, y)  # annotation is not a mandatory! So it is possible to assign as other types.
    print(z1, type(z1))  # annotation is not a mandatory! So it is possible to result in other types.
    z2 = func_test(99.8, 5)  # if second parameter was neglected, then it will bring out default value.
    print(z2, type(z2))


def iter_test():
    li = ['Happy', 'New', 'Year', '!!']
    for i in li:  # Iterate value
        print(i)
    for i in range(len(li)):  # Iterate index
        print(i)
    for i, v in enumerate(li):  # Iterate index, value
        print(i, v)
    for i, v in enumerate(li, 1):  # Iterate index, value but index starts as 1
        print(i, v)
    iter_li = iter(li)  # Using iterator
    print(type(iter_li))
    print(iter_li.__next__())
    print(next(iter_li))
    print(iter_li.__next__())
    print(iter_li.__next__())
    try:
        print(iter_li.__next__())  # When try nex() after iteration ended
    except StopIteration:
        print("No More Items!")


def card_conv(x: int, r: int) -> str:
    """ Convert from base 10 to base R """
    d = ''
    d_char = ''.join([chr(n) for n in range(ord('0'), ord('9') + 1)]+[chr(n) for n in range(ord('A'), ord('Z') + 1)])

    while x > 0:
        d += d_char[x % r]
        x //= r

    return d[::-1]


def card_conv_test():
    n, r = None, None
    while n is None:
        try:
            temp = int(input('Enter decimal number to convert: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    while r is None:
        try:
            temp = int(input(f'Convert decimal number {n} to base: ').strip())
            if temp < 2 or temp > 36:
                raise ValueError
            r = temp
        except ValueError:
            print('Base number should be within 2 to 26 by integer type!')
    result = card_conv(n, r)

    print(f'Base 10 number "{n}" ==> Base {r} number "{result}"')


def change(li, idx, val):  # No return
    li[idx] = val
    print('change() executed!')


def change_test():
    lst = [11, 22, 33, 44, 55]
    print('Before change():', lst)
    change(lst, 2, 'Changed!')  # Changed third value
    print('After change():', lst)  # Since list is mutable object, function modification affected the real object!


def is_decimal(prime: list, x: int):
    i = 1
    while prime[i]*prime[i] <= x:
        if x % prime[i]:
            return False
        i += 1
    return True


def find_all_decimal():
    prime = [2, 3]
    for k in range(5, 1001, 2):
        if is_decimal(prime, k):
            prime.append(k)
    print(f'Decimal numbers in "1001" : {prime}')


def deep_copy_example():
    x = [[1, 2, 3], [4, 5, 6]]
    y = x.copy()
    z = deepcopy(x)
    x[0][1] = 9  # Modification
    print("x=", x)
    print("y=", y)  # Affected by modification => (sallow copy) It has been copied at the sequence level
    print("z=", z)  # Not affected by modification => (deep copy) It has been copied at the component level


if __name__ == "__main__":
    # compare_lists()
    # sequence_computing()
    # find_maximum()
    # annotation_test()
    # iter_test()
    # card_conv_test()
    # change_test()
    # find_all_decimal()
    deep_copy_example()