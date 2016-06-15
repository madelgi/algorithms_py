from nose.tools import raises
from algorithms_py.utils.generate_list import generate_list
from algorithms_py.data_structures.lists.array_list import (
    ArrayList,
)


BASE_LIST = [4, 2, 11, 23, -19, 32, 123, 43, -76, 1, 3, 6]
ARRAY_LIST = ArrayList(BASE_LIST)


def check_equivalence(py_list, array_list):
    """Utility function for checking the equivalence of my linked list
    implementation and python's default list construct.
    """
    for i in xrange(array_list.numElts):
        if py_list[i] != array_list.vals[i]:
            return False
    return True


class TestArrayList:
    def setup(self):
        self.base_empty = []
        self.base_list = generate_list(size=100, negatives=True)
        self.array_list = ArrayList(list(self.base_list))
        self.array_empty = ArrayList(list([]))

    def test_create(self):
        assert check_equivalence(self.base_list, self.array_list)

    def test_prepend(self):
        prepend_base = [3] + self.base_list
        self.array_list.prepend(3)
        assert check_equivalence(prepend_base, self.array_list)

    def test_append(self):
        self.base_list.append(3)
        self.array_list.append(3)
        assert check_equivalence(self.base_list, self.array_list)

    def test_length(self):
        assert len(self.base_list) == self.array_list.length()
        assert len(self.base_list) == 100

    def test_search_pass(self):
        assert ARRAY_LIST.search(3) == 3

    @raises(ValueError)
    def test_search_fail(self):
        ARRAY_LIST.search(999)

    def test_delete_pass(self):
        ARRAY_LIST.delete(32)
        BASE_LIST.remove(32)
        assert check_equivalence(BASE_LIST, ARRAY_LIST)

    @raises(ValueError)
    def test_delete_fail(self):
        assert ARRAY_LIST.delete(999)

    def test_reverse(self):
        self.base_list.reverse()
        self.array_list.reverse()
        assert check_equivalence(self.base_list, self.array_list)
