from nose.tools import raises
from algorithms_py.data_structures.hashes.direct_address import (
    from_list,
)


class TestDirectAddressTable:
    def setup(self):
        self.base_list = [10, "hi", 31, 3.0, True]
        self.table = from_list(list(self.base_list))

    def test_search(self):
        assert self.table.search[0] is 10
        assert self.table.search[1] is 'hi'
        assert self.table.search[2] is 31
        assert self.table.search[3] is 3.0
        assert self.table.search[4] is True

    @raises(IndexError)
    def test_search_fail(self):
        self.table.search[31]
