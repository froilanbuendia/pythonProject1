"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        # todo
        if not self.has_edge(i, j):
            self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        # todo
        for k in range(len(self.adj[i])):
            if self.adj[i][k] == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        for k in range(len(self.adj[i])):
            if self.adj[i][k] == j:
                return True
        return False

    def out_edges(self, i) -> List:
        # todo
        return self.adj[i]

    def in_edges(self, i) -> List:
        # todo
        in_edg = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(j, i):
                in_edg.append(j)
        return in_edg

    def bfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n, np.bool_)
        q = ArrayQueue.ArrayQueue()
        traversal.append(r)
        seen[r] = True
        q.add(r)
        while q.size() > 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for i in range(0, len(neighbors)):
                neighbor = neighbors[i]
                if not seen[neighbor]:
                    traversal.append(neighbor)
                    seen[neighbor] = True
                    q.add(neighbor)
        return traversal


    def dfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n, np.bool_)
        stack = ArrayStack.ArrayStack()
        stack.push(r)
        while stack.size() > 0:
            current = stack.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            for neighbor in reversed(neighbors):
                if not seen[neighbor]:
                    stack.push(neighbor)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s




g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g)
print("BFS(0)", g.bfs(0))

# g = AdjacencyList(12)
# g.add_edge(0, 1)
# g.add_edge(0, 9)
# g.add_edge(1, 0)
# g.add_edge(1, 2)
# g.add_edge(1, 10)
# g.add_edge(1, 11)
# g.add_edge(2, 1)
# g.add_edge(2, 3)
# g.add_edge(2, 11)
# g.add_edge(3, 2)
# g.add_edge(3, 4)
# g.add_edge(4, 3)
# g.add_edge(4, 5)
# g.add_edge(4, 11)
# g.add_edge(5, 4)
# g.add_edge(5, 6)
# g.add_edge(6, 5)
# g.add_edge(6, 7)
# g.add_edge(6, 11)
# g.add_edge(7, 6)
# g.add_edge(7, 8)
# g.add_edge(7, 10)
# g.add_edge(8, 7)
# g.add_edge(8, 9)
# g.add_edge(9, 0)
# g.add_edge(9, 8)
# g.add_edge(9, 10)
# g.add_edge(10, 1)
# g.add_edge(10, 7)
# g.add_edge(10, 9)
# g.add_edge(10, 11)
# g.add_edge(11, 2)
# g.add_edge(11, 4)
# g.add_edge(11, 6)
# g.add_edge(11, 10)
#
# print(g)
# print("BFS(0):", g.bfs(0))
# print("Expected: [0, 1, 9, 2, 10, 11, 8, 3, 7, 4, 6, 5]")
# print("\nDFS(0):", g.dfs(0))
# print("Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")

