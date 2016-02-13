from algorithms_py.utils.generate_list import generate_list
from algorithms_py.algorithms.sort import bubble_sort, insertion_sort, merge_sort


class TestSortingAlgorithms:
    def setup(self):
        self.standard_list = generate_list(size=100)
        self.negative_list = generate_list(size=100, negatives=True)

    def test_bubble_sort(self):
        assert bubble_sort(self.standard_list) == sorted(self.standard_list)
        assert bubble_sort(self.negative_list) == sorted(self.negative_list)

    def test_insertion_sort(self):
        assert insertion_sort(self.standard_list) == sorted(self.standard_list)
        assert insertion_sort(self.negative_list) == sorted(self.negative_list)

    def test_merge_sort(self):
        assert merge_sort(self.standard_list) == sorted(self.standard_list)
        assert merge_sort(self.negative_list) == sorted(self.negative_list)
