"""
    Ch1 Basic of Data Structure and Sequences(기본 자료구조와 배열)
    * Skipped too simple examples

    * important notes
    1) Comparing logics of array is allowed.
        => check the function 'compare_lists'
    2) List and Tuple computations
        => check the function 'sequence_computing'
"""


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


if __name__ == "__main__":
    compare_lists()
    sequence_computing()
