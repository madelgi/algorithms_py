from algorithms_py.utils.generate_list import generate_list
from algorithms_py.algorithms.brute_force.bubble_sort import bubble_sort


class TestSortingAlgorithms:
    def setup(self):
        self.standard_list = generate_list(size=100)
        self.negative_list = generate_list(size=100, negatives=True)

    def test_bubble_sort_functionality(self):
        assert bubble_sort(self.standard_list) == sorted(self.standard_list)
        assert bubble_sort(self.negative_list) == sorted(self.negative_list)

    def test_bubble_sort_edge_cases(self):
        assert bubble_sort([]) == sorted([])
        assert bubble_sort([0]) == sorted([0])
        assert bubble_sort([0, 0]) == sorted([0, 0])
        assert bubble_sort([0, 0, 0]) == sorted([0, 0, 0])

    def test_bubble_sort_reflexive(self):
        assert bubble_sort(bubble_sort(self.standard_list)) == bubble_sort(self.standard_list)
        assert bubble_sort(bubble_sort(self.negative_list)) == bubble_sort(self.negative_list)
        assert bubble_sort(bubble_sort([])) == bubble_sort([])
