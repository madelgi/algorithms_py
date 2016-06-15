from algorithms_py.utils.generate_list import generate_list
from algorithms_py.algorithms.divide_conquer.insertion_sort import insertion_sort


class TestSortingAlgorithms:
    def setup(self):
        self.standard_list = generate_list(size=100)
        self.negative_list = generate_list(size=100, negatives=True)

    def test_insertion_sort_functionality(self):
        assert insertion_sort(self.standard_list) == sorted(self.standard_list)
        assert insertion_sort(self.negative_list) == sorted(self.negative_list)

    def test_insertion_sort_edge_cases(self):
        assert insertion_sort([]) == sorted([])
        assert insertion_sort([0]) == sorted([0])
        assert insertion_sort([0, 0]) == sorted([0, 0])
        assert insertion_sort([0, 0, 0]) == sorted([0, 0, 0])

    def test_insertion_sort_reflexive(self):
        assert insertion_sort(insertion_sort(self.standard_list)) == insertion_sort(self.standard_list)
        assert insertion_sort(insertion_sort(self.negative_list)) == insertion_sort(self.negative_list)
        assert insertion_sort(insertion_sort([])) == insertion_sort([])
