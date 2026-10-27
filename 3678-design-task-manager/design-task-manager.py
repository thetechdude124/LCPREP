import heapq
from typing import List

class TaskManager:

    '''

    we can keep a global dict that segregates users by the tasks
    so we have a dictionary mapping task id to its corresponding user and priority
    we keep a max heap to get the task with the highest pripotiy
    we use the dictionary as a method to keep the canonical version true

    '''

    def __init__(self, tasks: List[List[int]]):

        self.taskdict = {}
        self.maxheap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)


    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskdict[taskId] = [userId, priority]
        # because the task id is the tiebreaker
        heapq.heappush(self.maxheap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.taskdict[taskId][1] = newPriority
        heapq.heappush(self.maxheap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.taskdict[taskId]
        # lazy deletion from heap

    def execTop(self) -> int:
        while self.maxheap:
            # get the highest entry and check if its stale or not
            negP, negT = heapq.heappop(self.maxheap)
            taskId = -negT
            p = -negP
            if taskId in self.taskdict and self.taskdict[taskId][1] == p:
                res = self.taskdict[taskId][0]
                self.rmv(taskId)
                return res
        return -1