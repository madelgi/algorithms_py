class Stack(object):
    def __init__(self, vals=None):
        if not vals:
            self.vals = []
        else:
            self.vals = vals
        self.top = len(self.vals) - 1

    def __str__(self):
        lst = list(self.vals)
        s = ""
        while lst:
            s += str(lst.pop()) + "\n"
        return s[:-1]

    def push(self, val):
        self.vals.append(val)
        self.top += 1

    def peek(self):
        return self.vals[self.top]

    def pop(self):
        if self.is_empty():
            raise ValueError
        popped = self.vals[self.top]
        self.vals = self.vals[:self.top]
        self.top -= 1
        return popped

    def is_empty(self):
        if self.top < 0:
            return True
        return False
