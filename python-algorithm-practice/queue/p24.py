"""
    Problem 24: Implement Queue using Stacks

    Question: Using a stack, create a queue that applies following function
    * following function list:
        push(x), pop(), peek(), empty()
    Source: leetcode 232 (https://leetcode.com/problems/implement-queue-using-stacks/

"""
from common.common_function import test_function


# Solution: Using two stack to implement
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


if __name__ == "__main__":
    s_queue = MyQueue()
    test_function('push', s_queue.push, "Hello! I'm Input 1!!")
    test_function('push', s_queue.push, "Hello! I'm Input 2!!")
    test_function('pop', s_queue.pop)
    test_function('push', s_queue.push, "Hello! I'm Input 3!!")
    test_function('push', s_queue.push, "Hello! I'm Input 4!!")
    test_function('peek', s_queue.peek)
    test_function('empty', s_queue.empty)
    test_function('pop', s_queue.pop)
    test_function('pop', s_queue.pop)
    test_function('pop', s_queue.pop)
    test_function('empty', s_queue.empty)
