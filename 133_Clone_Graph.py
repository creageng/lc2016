


# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None

        stack = []
        d = {}
        newhead = UndirectedGraphNode(node.label)
        stack.append(node)
        d[node] = newhead

        while stack:
            curr = stack.pop()
            for neighbor in curr.neighbors:
                if neighbor not in d:
                    copy = UndirectedGraphNode(neighbor.label)
                    d[curr].neighbors.append(copy)
                    d[neighbor] = copy
                    stack.append(neighbor)
                else:
                    d[curr].neighbors.append(d[neighbor])

        return newhead








