from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        #store in graph
        graph = [[] for i in range(numCourses)]
        indegs = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegs[a] += 1

        # initialize queue
        q = deque()
        for i, v in enumerate(indegs):
            if v == 0:
                q.append(i)

        final_order = []
        while q:
            #pop FIFO
            vertex = q.popleft()
            final_order.append(vertex)

            for nbor in graph[vertex]:
                indegs[nbor] -= 1
                if indegs[nbor] == 0:
                    q.append(nbor)
        # cycle check
        if len(final_order) != numCourses:
            return []
        return final_order

