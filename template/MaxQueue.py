from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x : object):
        """
        adds an element to the end of this max queue
        INPUT: x the element to add

        if x > DLList head:
            replace the DLList to contain only x
        else:
            1) Beginning at the tail of DLList, remove all elements less than x
            2) Add x to the end of DLList


        Queue.add(x)
        if empty, x is also max:

        else:
            what is our max?
            what is the size of our second list
            if x > max:
                reassign NEW DLList
                add new max
            else:
                get tail of DLList
                while x > tail
                    remove the tail
                    n -= 1
                    get tail of DLList

                add to end x
        """
        n = len(self.max_deque)
        SLLQueue.add(self, x)
        if n == 0:
            self.max_deque.add_first(x)
        elif x > self.max_deque.get(0):
            self.max_deque = DLLDeque()
            self.max_deque.add_first(x)
        else:
            tail = self.max_deque.get(n - 1)
            while x > tail:
                if n == 0:
                    break
                self.max_deque.remove_last()
                n -= 1
                tail = self.max_deque.get(n - 1)
            self.max_deque.add_last(x)

    def remove(self) -> object:
        """
        removes and returns the element at the head of the max queue
        '1) remove from head of SLLQueue
        2) check if what was removed is also m the head of DLList. If yes, remove it there as well'

        r = removed from queue
        if r = max:
            remove mx
        """
        '''r = SLLQueue.remove(self)
        if r == max:
            SLLQueue.remove(max)
        return r'''
        r = SLLQueue.remove(self)
        if len(self.max_deque) > 0:
            if self.max_deque.get(0) == r:
                self.max_deque.remove_first()
        return r

    def max(self):
        """
        returns the maximum element stored in the queue
        return the head of the DLList
        """
        return self.max_deque.get(0)

# TESTER
'''mq = MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
'''
