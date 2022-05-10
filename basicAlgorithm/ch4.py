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
        => The module enables to add/delete the element bidirectionally from the sequence
    6) Notation for queue:
        a> enqueue: Add data
        b> dequeue: Remove data
        c> front: Direction from which removes data
        d> rear: Direction from which adds data
        e> priority queue: Higher priority data will be deleted first
            => Priority will be granted while adding data and data will be removed from the highest priority
            => Python module 'heapq' enables granting priority to queue
        f> ring buffer: The queue type that does not move element within array when dequeue executed
            => The front/rear are logical order but not physical order
            => The front/rear will be updated when enqueue/dequeue executed
            => The complexity of ring buffer executions are all the same as O(1)
            => Application: The program dequeues old data whenever new data enqueues(for the same number)

"""
from typing import Any
from ch3 import select_menu
from enum import Enum
from collections import deque

Menu_stack = Enum('Menu', ['Push', 'Pop', 'Peak', 'Find', 'Dump', 'Terminate'])

Menu_queue = Enum('Menu', ['Enqueue', 'Dequeue', 'Peak', 'Find', 'Dump', 'Terminate'])


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


class FixedQueue:

    class Empty(Exception):  # Subclass of both FixedStack and Exception
        pass

    class Full(Exception):  # Subclass of both FixedStack and Exception
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0  # Current number of data
        self.front = 0  # First element cursor
        self.rear = 0  # Last element cursor
        self.capacity = capacity  # Size of queue
        self.que = [None]*capacity  # Queue object(list)

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enqueue(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front == self.capacity
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity  # inorder to rotate properly
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity  # inorder to rotate properly
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0  #

    def dump(self) -> None:
        if self.is_empty():
            print('Queue is Empty!')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
                print()


def run_stack_menu(s: Any) -> None:
    while True:
        print(f'Current number of data: {len(s)} / {s.capacity}')
        menu = select_menu(Menu_stack)
        try:
            if menu == Menu_stack.Push:  # Add to the stack
                x = int(input('Enter the key to add: '))
                s.push(x)

            elif menu == Menu_stack.Pop:  # Remove from the stack and return the value removed
                s.pop()
                print(f'Popped data: {x}')

            elif menu == Menu_stack.Peak:  # Return the latest stacked value
                x = s.peek()
                print(f'Peeked data: {x}')

            elif menu == Menu_stack.Find:  # Return the target value
                x = int(input('Enter the value to search: '))
                if x in s:
                    print(f'The first index found: {s.find(x)}, Count: {s.count(x)}')
                else:
                    print(f'The value "{x}" does not exist!')

            elif menu == Menu_stack.Dump:  # Show the stack
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


def run_queue_menu(q: FixedQueue) -> None:
    while True:
        print(f'Current number of data: {len(q)} / {q.capacity}')
        menu = select_menu(Menu_queue)
        try:
            if menu == Menu_queue.Enqueue:  # Add to the stack
                x = int(input('Enter the data to enqueue: '))
                q.enqueue(x)

            elif menu == Menu_queue.Dequeue:  # Remove from the stack and return the value removed
                q.dequeue()
                print(f'Dequeued data: {x}')

            elif menu == Menu_queue.Peak:  # Return the latest stacked value
                x = q.peek()
                print(f'Peeked data: {x}')

            elif menu == Menu_queue.Find:  # Return the target value
                x = int(input('Enter the value to search: '))
                if x in q:
                    print(f'The first index found: {q.find(x)}, Count: {q.count(x)}')
                else:
                    print(f'The value "{x}" does not exist!')

            elif menu == Menu_queue.Dump:  # Show the stack
                q.dump()

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
    run_stack_menu(s)


def deque_stack_test():
    s = Stack(64)  # capacity = 64
    run_stack_menu(s)


def queue_test():
    q = FixedQueue(64)  # capacity = 64
    run_queue_menu(q)


if __name__ == '__main__':
    try_statement_test()
    fixed_stack_test()
    deque_stack_test()
    queue_test()
