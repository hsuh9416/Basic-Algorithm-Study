"""
    Problem 25: Design Circular Queue

    Question: Design a circular queue
    * Example:
        MyCircularQueue circularQueue = new MyCircularQueue(5) // size 5
        circularQueue.enQueue(10); // return True
        circularQueue.enQueue(20); // return True
        circularQueue.enQueue(30); // return True
        circularQueue.enQueue(40); // return True
        circularQueue.Rear(); // return 40
        circularQueue.isFull(); // return False
        circularQueue.deQueue(); // return True
        circularQueue.deQueue(); // return True
        circularQueue.enQueue(50); // return True
        circularQueue.enQueue(60); // return True
        circularQueue.Rear(); // return 60
        circularQueue.Front(); // return 30

    Source: leetcode 232 (https://leetcode.com/problems/design-circular-queue/

"""
from typing import Any
from common.common_function import test_function


# Solution: Using array
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.max_len = k
        self.p1 = 0
        self.p2 = 0

    def enqueue(self, value: Any) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.max_len
            return True
        else:
            return False

    def dequeue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.max_len
            return True

    def front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def is_empty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def is_full(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


if __name__ == "__main__":
    circularQueue = MyCircularQueue(5)
    test_function('enQueue', circularQueue.enqueue, 10)
    test_function('enQueue', circularQueue.enqueue, 20)
    test_function('enQueue', circularQueue.enqueue, 30)
    test_function('enQueue', circularQueue.enqueue, 40)
    test_function('Rear', circularQueue.rear)
    test_function('isFull', circularQueue.is_full)
    test_function('deQueue', circularQueue.dequeue)
    test_function('deQueue', circularQueue.dequeue)
    test_function('enQueue', circularQueue.enqueue, 50)
    test_function('enQueue', circularQueue.enqueue, 60)
    test_function('Rear', circularQueue.rear)
    test_function('Front', circularQueue.front)
