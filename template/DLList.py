from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        # todo
        if i < 0 or i > self.n: return None
        if i < self.n / 2:
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for k in range(self.n, i, -1):
                p = p.prev
        return p
        
    def get(self, i) -> np.object:
        # todo
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        # todo
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w : Node, x : np.object) -> Node:
        # todo
        if w == 0: raise ValueError()
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i : int, x : np.object)  :
        # todo
        #if i < 0 or i >= self.n: raise IndexError()
        return self.add_before(self.get_node(i), x)

    def _remove(self, w : Node) :
       # todo
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i :int) :
        if i < 0 or i >= self.n: raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x : np.object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        # todo
        if self.n == 1:
            return True
        elif self.n is None:
            raise IndexError()

        # Traverse through linked list from beginning and end
        # Find last node in list and store it
        # Traverse through beginning and end of list in parallel
        for i in range(0, self.n):
            if self[self.n - i - 1] == self[i]:
                pass
            else:
                return False
        return True

    def reverse(self):
        '''
        Key: change the order of nodes NOT the values
        stopping point for current loop
        prev
        curr
        temp
        head
        tail
        temp = curr.next
        curr.next = prev
        curr.prev = temp
        '''
        curr = self.dummy.next
        tail = self.dummy.prev
        for i in range(self.n // 2):
            temp = curr.x
            curr.x = tail.x
            tail.x = temp
            curr = curr.next
            tail = tail.prev

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
