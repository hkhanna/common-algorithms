class MyArray(object):
    """My implementation of an array"""

    def __init__(self, initial=[]):
        self.arr = initial
    
    def read(self, index):
        if index >= len(self.arr):
            raise LookupError 
        return self.arr[index]
    
    def insert(self, val, index=0):
        # index is where the value should be at the *end* of this function

        # Needs to add a spot at the end
        self.arr.append(None)

        # Convert negative indexes to positive ones
        if index < 0:
            index = len(self.arr) + index

        # Shift everything down
        for i in range(len(self.arr) - 1, index, -1):
            self.arr[i] = self.arr[i - 1]
        
        # Insert new item
        self.arr[index] = val

    def search(self, val):
        for i in range(len(self.arr)):
            if self.arr[i] == val:
                return i
        return -1

    def delete(self, index):
        # Convert negative indexes to positive ones
        if index < 0:
            index = len(self.arr) + index

        # Delete item
        self.arr[index] = None

        # Shift everything to fill in gap
        for i in range(index, len(self.arr) - 1):
            self.arr[i] = self.arr[i + 1]

        # Remove the empty cell at the end
        del self.arr[-1]

    def __repr__(self):
        return str(self.arr)

class PythonArray(object):
    """Use the python stdlib as much as possible"""
    def __init__(self, initial=[]):
        self.arr = initial

    def read(self, index):
        if index >= len(self.arr):
            raise LookupError 
        return self.arr[index]
 
    def insert(self, val, index=0):
        self.arr.insert(index, val)
    
    def search(self, val):
        try:
            return self.arr.index(val)
        except ValueError:
            return -1
    
    def delete(self, index):
        del self.arr[index]