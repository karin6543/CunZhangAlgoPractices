from collections import deque

class Solution():
    def bfs(self, graph, node):
        v = []
        q = [node]

        while q:
            prev = q.pop(0)

            for neighbor in graph[prev]:
                if neighbor not in v:
                    v.append(neighbor)
                    q.append(neighbor)
                    self.bfs(graph, neighbor)

    def bfsIterative(self, graph, node):
        v = []
        q = [node]

        while q:
            prev = q.pop(0)
            for neighbor in graph[prev]:
                if neighbor not in v:
                    v.append(neighbor)
                    q.append(neighbor)
                    

