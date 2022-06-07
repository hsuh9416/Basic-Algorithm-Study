"""
    Problem 23: Implement Stack using Queues

    Question: Using a queue, create a stack that applies following function
    * following function list:
        push(x), pop(), top(), empty()
    Source: leetcode 225 (https://leetcode.com/problems/implement-stack-using-queues/

"""
import collections
from common.common_function import test_function


# Solution: Using queue to resort the structure while executing push()
class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


if __name__ == "__main__":
    q_stack = MyStack()
    test_function('push', q_stack.push, "Hello! I'm Input Value 1!!")
    test_function('push', q_stack.push, "Hello! I'm Input Value 2!!")
    test_function('pop', q_stack.pop)
    test_function('push', q_stack.push, "Hello! I'm Input Value 3!!")
    test_function('push', q_stack.push, "Hello! I'm Input Value Top!!")
    test_function('pop', q_stack.top)
    test_function('empty', q_stack.empty)
    test_function('pop', q_stack.pop)
    test_function('pop', q_stack.pop)
    test_function('pop', q_stack.pop)
    test_function('empty', q_stack.empty)
