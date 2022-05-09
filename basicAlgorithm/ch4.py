"""
    Ch4 Stack and Que(스택과 큐)
    * Skipped too simple examples

    * important notes
    1) Stack pointer: the integer value represents the number of data stacked
        => In fixed stack, the stack pointer will be within range from 0 to capacity
        => However, there might be errors can result in stack pointer
           to be less than 0 or large tan capacity. => Therefore, compare by '<,>=' not '=='!
    2) Full structure of try statement
        a> try: The process to be tested
        b> except: The process to be run if target exception occurred
        c> else: The process to be run if no error has been found
        d> finally: The process should be run regardless of the exceptions
    3) __len__() function
        => By being defined within class, enabled to pass class type instances to the len() function
        => obj.__len__() --> len(obj)
    4) __contains__() function
        => By being defined within class, enabled to apply logical operator in
        => obj.__contains__(x) --> x in obj
    5) collection.deque
        => One of the Python built-in modules/libraries
        => The module enables to add/delete the element bidirectionally from the que

"""
from typing import Any
from ch3 import select_menu
from enum import Enum
from collections import deque

Menu = Enum('Menu', ['Push', 'Pop', 'Peak', 'Find', 'Dump', 'Terminate'])


def try_statement_test() -> None:
    print("*** NOTE: We ONLY accepts INTEGER NUMBER ***")
    try:
        a = int(input("Please enter INTEGER NUMBER: ").strip())
        print(f'You entered the number {a}.')
    except ValueError:
        print("You made an error!!")
    else:
        print("It seems no error has been occurred...")
    finally:
        print("Nonetheless, I will run this code!")


class FixedStack:

    class Empty(Exception):  # Subclass of both FixedStack and Exception
        pass

    class Full(Exception):  # Subclass of both FixedStack and Exception
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity  # Stack Object(Array)
        self.capacity = capacity  # Size of the stack
        self.ptr = 0  # Stack pointer

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:  # Look up to the latest data
        if self.is_full():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print('The stack is empty')
        else:
            print(self.stk[:self.ptr])


class Stack:

    def __init__(self, capacity: int = 256) -> None:
        self.capacity = capacity
        self.__stk = deque([], capacity)

    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def pop(self) -> Any:
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> int:
        print(list(self.__stk))


def run_menu(s: Any) -> None:
    while True:
        print(f'Current number of data: {len(s)} / {s.capacity}')
        menu = select_menu(Menu)
        try:
            if menu == Menu.Push:  # Add to the stack
                x = int(input('Enter the key to add: '))
                s.push(x)

            elif menu == Menu.Pop:  # Remove from the stack and return the value removed
                s.pop()
                print(f'Popped data: {x}')

            elif menu == Menu.Peak:  # Return the latest stacked value
                x = s.peek()
                print(f'Peeked data: {x}')

            elif menu == Menu.Find:  # Return the target value
                x = int(input('Enter the value to search: '))
                if x in s:
                    print(f'The first index found: {s.find(x)}, Count: {s.count(x)}')
                else:
                    print(f'The value "{x}" does not exist!')

            elif menu == Menu.Dump:  # Show the stack
                s.dump()

            else:
                break

        except ValueError:
            print('Please only enter integer numbers!!')
        except FixedStack.Full:
            print('The stack is full!!')
        except FixedStack.Empty:
            print('The stack is empty!!')
        else:
            print('The process done successful')
        finally:
            print('Return to the selection')


def fixed_stack_test():
    s = FixedStack(64)  # capacity = 64
    run_menu(s)


def deque_stack_test():
    s = Stack(64)  # capacity = 64
    run_menu(s)


if __name__ == '__main__':
    try_statement_test()
    fixed_stack_test()
    deque_stack_test()
