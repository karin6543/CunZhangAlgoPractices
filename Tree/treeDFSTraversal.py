class Solution():
    def dfs(self, node):
        v = []
        stack = [node]
        while stack:
            prev = stack.pop()
            v.append(prev)
            if prev.left:
                stack.append(prev.left)
            if prev.right:
                stack.append(prev.right)
