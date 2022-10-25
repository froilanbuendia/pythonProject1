from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i][j] = True

    def remove_edge(self, i : int, j : int):
        # todo
        if self.has_edge(i, j):
            self.adj[i][j] = False
            return True
        else:
            return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        # todo
        out = ArrayList.ArrayList()
        for j in range(len(self.adj[i])):
            if self.adj[i][j]:
                out.append(j)
        return out

    def in_edges(self, i) -> List:
        # todo
        in_ed = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(j, i):
                in_ed.append(j)
        return in_ed

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


# g = AdjacencyMatrix(6)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(0, 3)
# g.add_edge(2, 4)
# g.add_edge(4, 5)
# g.add_edge(1, 4)
# g.add_edge(4, 5)

# print(g)
# print(g.bfs(0))

g = AdjacencyMatrix(12)
g.add_edge(0, 1)
g.add_edge(0, 9)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(1, 10)
g.add_edge(1, 11)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(2, 11)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(4, 11)
g.add_edge(5, 4)
g.add_edge(5, 6)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(6, 11)
g.add_edge(7, 6)
g.add_edge(7, 8)
g.add_edge(7, 10)
g.add_edge(8, 7)
g.add_edge(8, 9)
g.add_edge(9, 0)
g.add_edge(9, 8)
g.add_edge(9, 10)
g.add_edge(10, 1)
g.add_edge(10, 7)
g.add_edge(10, 9)
g.add_edge(10, 11)
g.add_edge(11, 2)
g.add_edge(11, 4)
g.add_edge(11, 6)
g.add_edge(11, 10)

print(g)
print("BFS(0):", g.bfs(0))
print("Expected: [0, 1, 9, 2, 10, 11, 8, 3, 7, 4, 6, 5]")
print("\nDFS(0):", g.dfs(0))
print("Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")


