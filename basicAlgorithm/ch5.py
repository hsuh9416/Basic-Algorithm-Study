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


"""
# import math


def factorial(n: int) -> int:
    # return math.factorial(n)
    return 1 if n <= 0 else n * factorial(n - 1)


def gcd(x: int, y: int) -> int:  # Greatest common divisor(By Euclidean algorithm)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


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


if __name__ == '__main__':
    # basic_recursion_test()
    basic_recursion_test2()
