from nose.tools import raises
from algorithms_py.utils.generate_list import generate_list
from algorithms_py.data_structures.stacks.stack import (
    Stack,
)


BASE_LIST = [4, 2, 11, 23, -19, 32, 123, 43, -76, 1, 3, 6]
STACK = Stack(BASE_LIST)


def check_equivalence(py_list, stack):
    while py_list and stack.top > -1:
        if py_list.pop() is not stack.pop():
            return False
    return True


class TestStack:
    def setup(self):
        self.base_list = generate_list(size=100, negatives=True)
        self.stack = Stack(list(self.base_list))

    def test_create(self):
        assert check_equivalence(self.base_list, self.stack)

    def test_push(self):
        self.base_list.append(21)
        self.stack.push(21)
        assert check_equivalence(self.base_list, self.stack)

    def test_pop(self):
        item = self.stack.peek()
        assert self.stack.pop() is item

    @raises(ValueError)
    def test_pop_fail(self):
        Stack().pop()

    def test_peek(self):
        assert STACK.peek() == 6

    def test_is_empty(self):
        assert Stack().is_empty() is True
        assert self.stack.is_empty() is False
