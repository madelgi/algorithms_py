from nose.tools import raises
from collections import deque
from algorithms_py.utils.generate_list import generate_list
from algorithms_py.data_structures.queues.queue import (
    MyQueue,
)


BASE_LIST = [4, 2, 11, 23, -19, 32, 123, 43, -76, 1, 3, 6]
QUEUE = MyQueue(BASE_LIST)


def check_equivalence(py_queue, queue):
    if len(py_queue) is not queue.vals.length():
        return False

    while py_queue and queue.vals:
        if queue.dequeue() is not py_queue.pop():
            return False
    return True


class TestQueue:
    def setup(self):
        base_list = generate_list(size=100, negatives=True)
        self.py_queue = deque(list(base_list))
        self.queue = MyQueue(list(base_list))

    def test_create(self):
        assert check_equivalence(self.py_queue, self.queue)

    def test_enqueue(self):
        self.py_queue.appendleft(21)
        self.queue.enqueue(21)
        assert check_equivalence(self.py_queue, self.queue)

    def test_dequeue(self):
        assert QUEUE.dequeue() == 6
        assert QUEUE.dequeue() == 3
        assert QUEUE.dequeue() == 1
        assert QUEUE.dequeue() == -76

    @raises(ValueError)
    def test_dequeue_fail(self):
        MyQueue().dequeue()

    def test_is_empty(self):
        assert self.queue.is_empty() is False
        assert MyQueue().is_empty() is True
