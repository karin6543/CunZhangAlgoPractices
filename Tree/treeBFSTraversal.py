from collections import deque

class Solution():
    def traverse(self, node):
        v = []
        q = [node]
        while q:
            prev = q.pop(0)
            v.append(prev)
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)

# using collections.deques

    def traverseDeque(self, node):
        v = []
        q = deque(node)
        while q:
            prev = q.popleft()
            v.append(prev)
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)