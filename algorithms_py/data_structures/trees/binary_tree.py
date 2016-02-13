class Node(object):
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val


class BinaryTree(object):
    def __init__(self, val=None):
        self.val = val
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

    def insert(self, val):
        if not self.val:
            self.val = val
        elif val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinaryTree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinaryTree(val)

    def search(self, val):
        if self.val == val:
            return val

        if self.val < val:
            try:
                return self.right.search(val)
            except AttributeError:
                pass
        else:
            try:
                return self.left.search(val)
            except AttributeError:
                pass

    def maximum(self):
        """Return the maximum value in the tree.

        Args:
            None
        Returns:
            A number
        """
        if self.right:
            return self.right.maximum()
        else:
            return self.val

    def minimum(self):
        """Return the minimum value in the tree.

        Args:
            None
        Returns:
            A number
        """
        if self.left:
            return self.left.minimum()
        else:
            return self.val

    def balance(self):
        return 0

    def is_empty(self):
        """Determine whether the tree is empty.

        Args:
            None
        Returns:
            A boolean
        """
        if self.val:
            return False
        return True

    def is_balanced(self):
        """Determine whether the tree is balanced.

        Args:
            None
        Returns:
            A boolean.
        """
        if height(self) <= 1:
            return True
        else:
            if self.left is None:
                return height(self.right) <= 1
            if self.right is None:
                return height(self.left) <= 1
            balanced_subs = self.left.is_balanced() and self.right.is_balanced()
            balanced_height = abs(height(self.left) - height(self.right)) <= 1
            return balanced_subs and balanced_height


def in_order(tree):
    """
    Perform an in-order tree walk
    """
    if tree:
        in_order(tree.left)
        print tree.val
        in_order(tree.right)


def height(tree):
    """
    Return the height of a tree.
    """
    if tree.is_empty():
        return 0
    else:
        if tree.right is None and tree.left is None:
            return 1
        elif tree.left is None:
            return 1 + height(tree.right)
        elif tree.right is None:
            return 1 + height(tree.left)
        else:
            return max(1 + height(tree.right), 1 + height(tree.left))


def main():
    t = BinaryTree(10)
    t.insert(7)
    t.insert(13)
    t.insert(6)
    t.insert(8)
    t.insert(12)
    t.insert(14)
    t2 = BinaryTree(9)
    t2.insert(8)
    t2.insert(7)
    t2.insert(6)
    t2.insert(5)
    t2.insert(4)
    print t.maximum()
    print t2.maximum()
    print t.minimum()
    print t2.minimum()
    print t2.search(5)
    print t2.search(9)
    print t.search(6)
    print t.search(5)


if __name__ == '__main__':
    main()
