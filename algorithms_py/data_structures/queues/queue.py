import sys
sys.path.insert(0, '/Users/maxdelgiudice/learning/concepts/data_structures/lists')
import doubly_linked_list as dll


class MyQueue(object):
    """A queue implemented as a doubly linked list.
    """
    def __init__(self, vals=None):
        if vals is None:
            self.vals = dll.from_list([])
        else:
            self.vals = dll.from_list(vals)

    def __str__(self):
        return str(self.vals)

    def enqueue(self, val):
        """Add an element to the back of the queue.
        """
        self.vals.prepend(val)

    def dequeue(self):
        """Remove the element from the front of the queue and return it.
        """
        if self.vals.length() is 0:
            raise ValueError("Queue is empty")
        dequeued = self.vals.last.val
        self.vals.last = self.vals.last.prev
        return dequeued

    def is_empty(self):
        """Check if a queue is empty.
        """
        if self.vals.length() is 0:
            return True
        return False
