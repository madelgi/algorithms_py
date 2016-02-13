from algorithms_py.utils.generate_list import generate_list
from algorithms_py.data_structures.lists.singly_linked_list import (
    from_list,
    SinglyLinkedList,
)

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


class TestSinglyLinkedList:
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
