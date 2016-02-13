from algorithms_py.utils.generate_list import generate_list
from algorithms_py.data_structures.hashes import direct_address_table


class TestDirectAddressTable:
    def setup(self):
        self.base_list = generate_list(size=100, negatives=True)
        self.table = direct_address_table.from_list(self.base_list)

    def test_something(self):
        pass
