class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self._insert(data, self.head)

    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data)

        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.left = Node(data)

