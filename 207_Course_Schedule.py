
# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# For example:

# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """

#         degrees = [0] * numCourses
#         childs = [[] for x in range(numCourses)]

#         for pre in prerequisites:
#           degrees[pre[0]] += 1
#           childs[pre[1]].append(pre[0])

#         courses = set(range(numCourses))
#         flag = True

#         while flag and len(courses):
#           flag = False
#           removeList = []

#           for course in courses:
#               if degrees[course] == 0:
#                   for child in childs[course]:
#                       degrees[child] -= 1
#                   removeList.append(course)
#                   flag = True

#           for course in removeList:
#               courses.remove(course)

#         return len(courses) == 0

# This is a classic Graph topology sorting problem, but an easy version. 
# We don't have to store the sort, in other words, we only need to detect 
# if exists cycle in a directed graph.

# Both DFS and BFS can be used to solve this problem.

# First of all, we need to get a representation of the graph, 
# either adjacency matrix or adjacency list is OK. In my code, you can see both ways. 
# But note that, when the number of vertex is large, adjacency matrix usually is NOT 
# a good option.

# In DFS, the general idea, is to search each vertex in the graph recursively, if
#  the current vertex has been visited in this search, then there must be a cycle. 
#  Be careful with the status of each vertex, here in my code, it has three states:  
#  unvisited (=0), visited(=1), searching(=-1). The third states is to detect the existence of cycle, while the 2nd state indicate that the vertex is already checked and there is no cycle.

# In BFS, the idea is much easier.  We store the indegree of each vertex, push the vertices with 0 indegree in stack (remember general BFS framwork?).  Every time, pop the stack and set indegree of connected vertices -1. In the end, if the number of popped out vertices is less than the total number of vertices in the original graph, there is cycle.

# BFS
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        childs = [[] for i in range(numCourses)]
        # indegree
        indegree = [0 for i in range(numCourses)]

        for pre in prerequisites:
            if pre[0] not in childs[pre[1]]:
                indegree[pre[0]] += 1
                childs[pre[1]].append(pre[0])
        
        stack = []
        # push the vertices with 0 indegree in stack 
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
                
# Every time, pop the stack and set indegree of connected vertices -1. 
        ct = 0
        while stack:
            parent = stack[0]
            stack.pop(0)
            ct += 1
            for child in childs[parent]:
                indegree[child] -= 1
                # become parent
                if indegree[child] == 0:
                    stack.append(child)

        if ct < numCourses:
            return False
        else:
            return True




# DFS
class Solution(object):

# # unvisited (=0), visited(=1), searching(=-1).
#  The 3rd states is to detect the existence of cycle, 
#  while the 2nd state indicate that the vertex is already checked and there is no cycle.
    
    def dfs(self, v, visit, gr):
        if visit[v] == 1:
            # can finish
            return True

        visit[v] = -1
        for i in gr[v]:
            if visit[i] == -1 or not self.dfs(i, visit, gr):
                return False
        
        visit[v] = 1
        return True

    def canFinish(self, numCourses, prerequisites):
        gr = [[] for i in range(numCourses)]
        visit = [0 for i in range(numCourses)]

        for p in prerequisites:
            if p[0] not in gr[p[1]]:
                gr[p[1]].append(p[0])

        for v in range(numCourses):
            if visit[v] != 1:
                if not self.dfs(v, visit, gr):
                    return False
        return True




















