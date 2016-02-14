from nose.tools import raises
from algorithms_py.utils.generate_list import generate_list
from algorithms_py.data_structures.lists.doubly_linked_list import (
    from_list,
)


BASE_LIST = [4, 2, 11, 23, -19, 32, 123, 43, -76, 1, 3, 6]
LINKED_LIST = from_list(BASE_LIST)


def check_equivalence(py_list, linked_list):
    """Utility function for checking the equivalence of my linked list
    implementation and python's default list construct.
    """
    current_node = linked_list.head
    for i in xrange(len(py_list)):
        if py_list[i] != current_node.val:
            return False
        current_node = current_node.next
    return True


class TestDoublyLinkedList:
    def setup(self):
        self.base_list = generate_list(size=100, negatives=True)
        self.linked_list = from_list(self.base_list)

    def test_create(self):
        assert check_equivalence(self.base_list, self.linked_list)

    def test_prepend(self):
        prepend_base = [3] + self.base_list
        self.linked_list.prepend(3)
        assert check_equivalence(prepend_base, self.linked_list)

    def test_append(self):
        self.base_list.append(3)
        self.linked_list.append(3)
        assert check_equivalence(self.base_list, self.linked_list)

    def test_length(self):
        assert len(self.base_list) == self.linked_list.length()
        assert len(self.base_list) == 100

    def test_search_pass(self):
        assert LINKED_LIST.search(3).val == 3

    @raises(ValueError)
    def test_search_fail(self):
        LINKED_LIST.search(999)

    def test_delete_pass(self):
        LINKED_LIST.delete(32)
        BASE_LIST.remove(32)
        assert check_equivalence(BASE_LIST, LINKED_LIST)

    @raises(ValueError)
    def test_delete_fail(self):
        assert LINKED_LIST.delete(999)

    def test_reverse(self):
        self.base_list.reverse()
        self.linked_list.reverse()
        assert check_equivalence(self.base_list, self.linked_list)
