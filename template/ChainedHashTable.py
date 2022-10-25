from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        if key == None: raise IndexError()
        h = self.t[self._hash(key)]
        for i in range(len(h)):
            if h.get(i).key == key:
                return h.get(i).value

    def add(self, key : object, value : object) :
        if self.find(key) != None:
            return False
        if self.n + 1 > len(self.t):
            self.resize()
        x = ChainedHashTable.Node(key, value)
        self.t[self._hash(key)].append(x)
        self.n += 1
        return True

    def remove(self, key : int)  -> object:
        # todo
        if self.find(key) == None: return None
        else:
            hash_value = self._hash(key)
            l = self.t[hash_value]
            for i in range(len(l)):
                if l.get(i).key == key:
                    l.remove(i)
                    self.n -= 1
                    if len(self.t) >= 3 * self.n:
                        self.resize()
                    return True
            return False
    
    def resize(self):
        # todo
        # len(self.t[hash_value])
        # self.t[hash_value].size()
        # when do we increment self.n
        # if we are at max for our table increment
        # if not decrement
        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1
        a = self.alloc_table(2 ** self.d)
        for j in range(len(self.t)):
            for i in range(len(self.t[j])):
                a[self._hash(self.t[j].get(i).key)].add(0, self.t[j].get(i))
        self.t = a

    def __str__(self):
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += "(" + str(k.key) + ", " + str(k.value) + "); "
            s += "\n"
        return s

    '''
     def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
    '''



