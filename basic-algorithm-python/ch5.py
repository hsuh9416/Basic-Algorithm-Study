"""
    Ch5 Recursive algorithm(재귀 알고리즘)
    * Skipped too simple examples

    * important notes
    1) Recursion: Defining a problem in terms of itself(Referencing itself)
    2) Direct recursion: recalls itself
       Indirect recursion: recalls the different function and the function recalls itself
    3) The greatest common divisor using recursion
        => Set two number as each side of a rectangle
        => Divide the bigger number by the smaller number(**)
        => left rectangle will consist two sides: the smaller number, the remainder after division(**)
        => At the point of no remainder, the smaller number used for division will be the greatest common divisor
    4) Approach of recursive algorithm
        => genuinely recursive function: function that executes recursive calls multiple times
        a> Top-down analysis: From first function to last function to be reached
        b> Bottem-up analysis: From first trial to last commitment
        c> In order to transform function from recursive to non-recursive
            => The variable from the previous execution should be temporary store
            => Use stack to store data
        d> Branching method: Dividing procedure to illustrate combinations
        e> Bounding method: Removing unnecessary branches to reduce the number of combinations
        f> Branching and bounding method: Combining bounding and branching

"""
# import math
from ch4 import Stack


def factorial(n: int) -> int:
    # return math.factorial(n)
    return 1 if n <= 0 else n * factorial(n - 1)


def gcd(x: int, y: int) -> int:  # Greatest common divisor(By Euclidean algorithm)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def recur(n: int) -> int:  # Genuinely recursive function
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)


def non_recur(n: int) -> int:  # None recursive function acts the same as recursive function
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break


def move(disk_num: int, depart: int, arrive: int) -> None:
    if disk_num > 1:  # Moving the other disks to the middle tower
        move(disk_num - 1, depart, 6 - depart - arrive)  # Since 1+2+3=6, next arrival be at the remained tower

    print(f'Move [{disk_num}] from {depart} to {arrive}')  # Moving the last dist to the target tower

    if disk_num > 1:
        move(disk_num - 1, 6 - depart - arrive, arrive)  # Moving the other disks to the target tower


def put(pos: list) -> None:
    for j in range(8):
        for i in range(8):
            print('O' if pos[i] == j else 'X', end='')
        print()
    print()


def set_queen(pos: list, flag_a: list, flag_b: list, flag_c: list, i: int) -> None:
    for j in range(8):
        if (
            not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 7]
        ):
            pos[i] = j
            if i == 7:
                put(pos)
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set_queen(pos, flag_a, flag_b, flag_c, i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False


def basic_recursion_test():
    n = None
    while n is None:
        try:
            temp = int(input('Enter numbers to calculate its factorial: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    print(f'{n}! = {factorial(n)}')


def basic_recursion_test2():
    print('Find the greatest common divisor of two numbers!')
    m, n = None, None
    while m is None or n is None:
        try:
            temp = int(input('Enter the first number: ').strip())
            if temp < 0:
                raise TypeError
            m = temp
            temp = int(input('Enter the second number: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    print(f'The greatest common divisor of {m} and {n} is {gcd(m, n)}')


def basic_recursion_test3():
    n = None
    while n is None:
        try:
            temp = int(input('Enter the first number: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')

    print('*' * 20 + 'Recursive Function' + '*' * 20)
    recur(n)

    print('*' * 20 + 'Non Recursive Function' + '*' * 16)
    non_recur(n)


def hanoi_test():
    print('Play Tower of Hanoi:)')
    n = None
    while n is None:
        try:
            temp = int(input('Enter the number of disks: ').strip())
            if temp < 0:
                raise TypeError
            n = temp
        except ValueError:
            print('Enter integer number only!')
        except TypeError:
            print(f'Enter the bigger value then 0!')
    move(n, 1, 3)


def eight_queen_test():
    pos = [0] * 8  # Position of queen from each column
    flag_a = [False] * 8  # Checking whether queen was placed from each row
    flag_b = [False] * 15  # Checking whether queen was placed diagonal(/)
    flag_c = [False] * 15  # Checking whether queen was placed diagonal(\)
    set_queen(pos, flag_a, flag_b, flag_c, 0)


if __name__ == '__main__':
    basic_recursion_test()
    basic_recursion_test2()
    hanoi_test()
    eight_queen_test()
