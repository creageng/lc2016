class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        self.childs = [[] for i in range(numCourses)]
        self.color = ['white' for i in range(numCourses)]
        self.order = []

        #search for all the childs for parents
        for i in range(len(prerequisites)):
            [v, u] = prerequisites[i]
            if v not in self.childs[u]:
                self.childs[u].append(v)

        for i in range(numCourses):
            if not self.canFinish(i):
                return []

        return self.order


    def canFinish(self, u):
        if self.color[u] == "black":
            return True

        if self.color[u] == "grey":
            return False

        self.color[u] = "grey"
        for v in self.childs[u]:
            if not self.canFinish(v):
                return False

        self.order.insert(0, u)
        self.color[u] = 'black'
        return True 