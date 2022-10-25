#import numpy as np
#import ArrayStack
#import BinaryTree
#import ChainedHashTable
#import DLList
#import operator
import numpy as np
import ArrayStack


class Calculator:
    def __init__(self) :
        #self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
        self.dict = None

    def set_variable(self, k :str, v : float):
        self.dict.add(k, v)
        
    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        valid = True
        i = 0
        while i < len(s) and valid:
            current = s[i]
            if current == "(":
                stack.push(current)
            elif current == ")":
                if len(stack) == 0:
                    valid = False
                else:
                    stack.pop()
            i += 1
        if len(stack) == 0:
            return valid

    def build_parse_tree(self, exp: str) -> str:
        #to do
        pass
    '''def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        pass '''

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        
        

'''
s = ')(3 + 4)( *2 + 1'
#stack - push pop
#input is a string
# all we care about i ()
for char in s:
    if char = ();
        # we only need one stack

if check our stack:
'''