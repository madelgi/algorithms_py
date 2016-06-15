class Element(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val


class DirectAddressTable(object):
    def __init__(self, size, vals=None):
        """
        Initialize a direct address table with keys drawn from a universe
        of size `size`.
        """
        self.size = size
        self.table = [None]*size

    def __str__(self):
        string = "{"
        for elt in self.table:
            if elt:
                string += str(elt.key) + ": " + str(elt.val) + ", "

        if string == "{":
            return "{}"

        return string[:-2] + "}"

    def search(self, key):
        """Return the value at a certain key in the direct address table.
        """
        if key >= self.size:
            raise IndexError
        return self.table[key]

    def insert(self, elt):
        """Insert an element into our direct address table.
        """
        if elt.key >= self.size:
            raise IndexError
        self.table[elt.key] = elt

    def delete(self, elt):
        """Remove an element from our direct address table.
        """
        try:
            self.table[elt.key] = None
        except IndexError:
            pass

    def _set_vals(self, vals):
        self.vals = vals


def from_list(lst):
    """Create a direct address table from a list.
    """
    list_len = len(lst)
    direct_address_table = DirectAddressTable(list_len)
    direct_address_table._set_vals(lst)
    return direct_address_table
