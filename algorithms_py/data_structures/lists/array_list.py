class ArrayList(object):
    def __init__(self, vals=None):
        if not vals:
            self.vals = [0]*16
            self.numElts = 0
        else:
            self.vals = vals
            self.numElts = len(vals)

    def __str__(self):
        string = "["
        i = 0
        while i < self.numElts-1:
            string += str(self.vals[i]) + ", "
            i += 1
        string += str(self.vals[i]) + "]"
        return string

    def prepend(self, val):
        new_array = [0]*len(self.vals)
        if self.numElts == len(self.vals):
            new_array *= 2
        new_array[0] = val
        for i in xrange(0, self.numElts):
            new_array[i+1] = self.vals[i]

        self.numElts += 1
        self.vals = new_array

    def append(self, val):
        list_length = len(self.vals)

        if self.numElts >= list_length:
            # Copy values to a bigger array if necessary.
            biggerList = [0]*(2*list_length)
            i = 0
            while i < list_length:
                biggerList[i] = self.vals[i]
                i = i+1
            self.vals = biggerList

        self.vals[self.numElts] = val
        self.numElts = self.numElts + 1

    def length(self):
        return self.numElts

    def search(self, val):
        for i in range(self.numElts):
            if self.vals[i] == val:
                return val
        raise ValueError("Value not found, br.")

    def delete(self, val):
        for i in xrange(self.numElts):
            # we just delete the first instance of the element.
            if self.vals[i] == val:
                if i == self.numElts:
                    self.vals = self.vals[:self.numElts]
                else:
                    self.vals = self.vals[:i] + self.vals[i+1:]
                self.numElts -= 1
                return
        raise ValueError("Value not found, br.")

    def reverse(self):
        self.vals = self.vals[:self.numElts][::-1] + self.vals[self.numElts:]
