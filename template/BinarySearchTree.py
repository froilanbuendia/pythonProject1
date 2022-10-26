from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def clear(self):
        self.r = None
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = None
        return u

    def find_eq(self, x: object) -> object:
        # todo
        u = self.r
        while u != None:
            if x < u.x:
                u = u.left
            elif x > u.x:
                u = u.right
            else:
                return u
        return u

    def find_last(self, x: object) -> BinaryTree.Node:
        # todo
        w = self.r
        prev = None
        while w != None:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev

    def find(self, x: object) -> object:
        # todo
        w = self.r
        z = None
        while w != None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return z

    def add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        # todo
        if p == None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def add_node(self, u: BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)

    def add(self, key: object, value: object) -> bool:
        # todo
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))

    def get(self, key: object) -> object:
        # todo
        #print("key:", key)
        if self.n is None: return None
        w = self.find_last(key)
        if w is not None and key == w.x:
            return w.v
        return None

    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left != None:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != None:
            s.parent = p
        self.n -= 1

    def remove_node(self, u: BinaryTree.Node):
        # todo
        if u is not None:
            if u.left == None or u.right == None:
                self.splice(u)
            else:
                w = u.right
                while w.left != None:
                    w = w.left
                u.x = w.x
                u.v = w.v
                self.splice(w)
            return u.v
        return None

    def remove(self, x: object) -> bool:
        # todo
        '''p = self.find_last(x)
        if self.n == None: raise ValueError
        if p != None and x == p.x:
            self.remove_node(p)
            return p.v
        raise ValueError'''
        if self.n is None: raise ValueError
        w = self.find_last(x)
        #print("w: ", w)
        #print("x: ", x)
        #print("w.x: ", w.x)
        if w != None and x == w.x:
            self.remove_node(w)
            return w.v
        raise ValueError

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.x
            u = self.next_node(u)

# test = BinarySearchTree()

'''print(test.get(2))
test.add(3, "third")
test.add(2, "second")
test.add(1, "first")
print(test.size())
print(test.size2())
print(test.get(2))
print(test.find_eq(2.5))
print(test.find_last(2.5).v)
print(test.find(2.5).v)
test.remove(3)
print(test.size())
print(test.size2())
print(test.get(3))
test.add(3, "third")
test.add(5, "fifth")
test.add(4, "fourth")
print(test.size())
print(test.find_eq(3.4))
print(test.find_last(3.4).v)
print(test.find(3.4).v)
print(test.height())
print(test.in_order())
'''
# test.add(1, 'B')
# test.add(25, 'Z')
# test.add(3, 'D')
# test.add(12, 'M')
# test.add(13, 'N')
# test.add(23, 'X')
# test.add(21, 'V')
# test.add(19, 'T')
# test.add(13, 'N')
# test.add(0, 'A')
# test.add(18, 'S')
# print("bf: ", test.bf_traverse())
# print("test: ", test.pre_order())