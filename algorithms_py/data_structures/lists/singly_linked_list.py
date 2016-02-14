class Node(object):

    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node

    def set_next(self, new_next):
        self.next = new_next


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        x = self.head
        string = "["
        while x.next is not None:
            string += str(x.val) + ", "
            x = x.next

        return (string + str(x.val) + "]")

    def prepend(self, val):
        """ Insert a value to the front of the list. """
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, val):
        """ Insert a value to the end of the list. """
        new_node = Node(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        """ Get the length of the list. """
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next

        return total

    def search(self, val):
        """ See if a certain value is contained within a list. """
        current = self.head
        found = False
        while current and found is False:
            if current.val == val:
                found = True
                break
            current = current.next

        if not found:
            raise ValueError("Value not present.")
        return current

    def delete(self, val):
        """ Delete the first node with value val """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.val == val:
                found = True
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("Can't delete what's not there br.")

        if previous is None:
            self.head = current.next
        else:
            previous.set_next(current.next)

    def reverse(self):
        """Reverse the list.
        """
        def reverse_help(current, last):
            if current is None:
                return last

            next_node = current.next
            current.next = last
            return reverse_help(next_node, current)

        self.head = reverse_help(self.head, None)


def from_list(lst):
    """Convert a python list to a SingleLinkedList.

    Args:
        lst: A python list.

    Returns:
        An equivalent SinglyLinkedList.
    """
    reverse = lst[::-1]
    sll = SinglyLinkedList()
    for x in reverse:
        sll.prepend(x)
    return sll
