import numpy as np
import random 
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        if self.n == 0:
            raise IndexError()
        rand_index = random.randint(self.j, self.n - 1)
        f_element = self.a[self.j]
        y = self.a[rand_index]
        self.a[rand_index] = f_element
        self.a[0] = y
        super().remove()
        return y

    '''
    we want to reassignment to change randomly selected index to be j
    swap random i with position
    
    holder = target 1
    target 1 = target 2
    target 2 = holder
    '''
     




