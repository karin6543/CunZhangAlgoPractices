class Solution:
    def __init__(self):
        self.v = []
        self.res = []

    def dfs(self, graph, node):
        if node is None:
            return None
        self.res.append(node)
        for neighbor in graph[node]:
            if node not in self.v:
                self.v.append(node)
                self.dfs(graph, neighbor)

    def dfsInterative(self, node, graph):
        stack = [node]
        v=[]

        while stack:
            prev = stack.pop()
            for neighbor in graph[prev]:
                if prev not in v:
                    v.append(prev)
                    stack.append(neighbor)