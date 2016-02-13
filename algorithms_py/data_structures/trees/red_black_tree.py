class Node(object):
    def __init__(self, data=None, color=False):
        """
        Initialize a red-black tree. A color of False indicates a black node,
        and True indicates a red node.
        """
        self.data = data
        self.color = color


class RedBlackTree(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        s = ""
        s += str(self.val) + " "
        if self.left is None:
            s += "N "
        else:
            s += str(self.left)
        if self.right is None:
            s += "N "
        else:
            s += str(self.right)
        return s
