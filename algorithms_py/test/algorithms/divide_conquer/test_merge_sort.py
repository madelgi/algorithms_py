from algorithms_py.utils.generate_list import generate_list
from algorithms_py.algorithms.divide_conquer.merge_sort import merge_sort


class TestSortingAlgorithms:
    def setup(self):
        self.standard_list = generate_list(size=100)
        self.negative_list = generate_list(size=100, negatives=True)

    def test_merge_sort_functionality(self):
        assert merge_sort(self.standard_list) == sorted(self.standard_list)
        assert merge_sort(self.negative_list) == sorted(self.negative_list)

    def test_merge_sort_edge_cases(self):
        assert merge_sort([]) == sorted([])
        assert merge_sort([0]) == sorted([0])
        assert merge_sort([0, 0]) == sorted([0, 0])
        assert merge_sort([0, 0, 0]) == sorted([0, 0, 0])

    def test_merge_sort_reflexive(self):
        assert merge_sort(merge_sort(self.standard_list)) == merge_sort(self.standard_list)
        assert merge_sort(merge_sort(self.negative_list)) == merge_sort(self.negative_list)
        assert merge_sort(merge_sort([])) == merge_sort([])

