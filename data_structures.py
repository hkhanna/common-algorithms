class BaseDataStructure(object):
    def __init__(self, _=None):
        pass

    def call(self, fn_name, *args):
        try:
            fn = getattr(self, fn_name)
        except AttributeError:
            return None
        return fn(*args)

class MyArray(BaseDataStructure):
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

        return val

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

        return index

    def __repr__(self):
        return str(self.arr)

class PythonArray(BaseDataStructure):
    """Use the python stdlib as much as possible"""
    def __init__(self, initial=[]):
        self.arr = initial

    def read(self, index):
        if index >= len(self.arr):
            raise LookupError 
        return self.arr[index]
 
    def insert(self, val, index=0):
        self.arr.insert(index, val)
        return val
    
    def search(self, val):
        try:
            return self.arr.index(val)
        except ValueError:
            return -1
    
    def delete(self, index):
        del self.arr[index]
        return index


class MyHashTable(BaseDataStructure):
    """My implementation of a hash table"""
    def __init__(self, initial={}):
        self.cells = int(len(initial) * 0.7) # load factor of 0.7

        self.ht = [[]] * self.cells
        for key, val in initial.items():
            self.insert(key, val)

    def read(self, key):
        # Search and read are conceptually the same
        return None

    def insert(self, key, val):
        cell = self.getcell(key)
        self.ht[cell].append((key, val))
        return val
    
    def search(self, key):
        cell = self.getcell(key)
        for k, v in self.ht[cell]: # Each cell stores an array of key, val tuples.
            if k == key:
                return v
        return False

    def delete(self, key):
        cell = self.getcell(key)
        for index, (k, _) in enumerate(self.ht[cell]):
            if k == key:
                del self.ht[cell][index]
        return key

    def getcell(self, key):
        hashcode = ''
        for s in str(key):
            hashcode += str(ord(s)) # this is to handle in case either a string or an int is passed
        cell = int(hashcode) % self.cells
        return cell


class PythonHashTable(BaseDataStructure):
    """A python dict"""
    def __init__(self, initial={}):
        self.ht = initial

    def read(self, key):
        # Search and read are conceptually the same
        return None

    def insert(self, key, val):
        # Ignore collisions
        self.ht[key] = val
        return val

    def search(self, key):
        try:
            return self.ht[key]
        except KeyError:
            return False

    def delete(self, key):
        try:
            del self.ht[key]
            return key
        except KeyError:
            return False


class MyStack(BaseDataStructure):
    """My implementation of a stack"""
    def __init__(self, initial=[]):
        self.arr = initial
    
    def remove(self):
        index = len(self.arr) - 1
        val = self.arr[index]
        del self.arr[index]
        return val
    
    def add(self, item):
        self.arr.append(None) # Insert spot at end
        index = len(self.arr) - 1
        self.arr[index] = item
        return item
    
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

class MyQueue(BaseDataStructure):
    """My implementation of a queue"""
    def __init__(self, initial=[]):
        self.arr = initial
    
    def add(self, item):
        self.arr.append(None) # insert spot at end
        for index in range(len(self.arr)):
            new_index = len(self.arr) - 1 - index
            old_index = new_index - 1
            self.arr[new_index] = self.arr[old_index]
        self.arr[0] = item
        return item

    def remove(self):
        index = len(self.arr) - 1
        val = self.arr[index]
        del self.arr[index]
        return val

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

class MySet(BaseDataStructure):
    pass

class PythonSet(BaseDataStructure):
    pass

class MyOrderedArray(BaseDataStructure):
    pass

class MyLinkedList(BaseDataStructure):
    pass

class MyDoublyLinkedListQueue(BaseDataStructure):
    pass

class MyBST(BaseDataStructure):
    pass

class MyMaxHeap(BaseDataStructure):
    pass

class MyTrie(BaseDataStructure):
    pass
