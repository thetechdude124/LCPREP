import heapq
from collections import defaultdict

class TaskManager:

    '''
    General approach: we can use a max heap to rank the priorities
    However, we'd like to maintain O(log n) for edit and remove, so we 
    can't manually go and traverse the heap since we don't have a L->R ordering
    invariant (just a height invariant)

    Strategy: remove/edit hashmap instead 
    then for exec top check if that node was supposed to be removed or not (or if its outdated)
    since the state doesn't matter until we actually try and execute

    '''

    def __init__(self, tasks: List[List[int]]):
        
        #store in heap + dict
        self.pheap = []
        self.task_dict = defaultdict(tuple)
        for task in tasks:
            heapq.heappush(self.pheap, (-task[2], -task[1], task[0]))
            # taskid -> (user id, priority)
            self.task_dict[task[1]] = (task[0], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_dict[taskId] = (userId, priority)
        heapq.heappush(self.pheap, (-priority, -taskId, userId))
        
    def edit(self, taskId: int, newPriority: int) -> None:
        #edit the dictionary version
        self.task_dict[taskId] = (self.task_dict[taskId][0], newPriority)
        #add this as a new element to the heap
        self.add(self.task_dict[taskId][0], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # remove the dictionary version
        del self.task_dict[taskId]

    def execTop(self) -> int:

        #get top of the heap, check if valid, if not continue popping
        while len(self.pheap) != 0:
            (p, taskId, userId) = heapq.heappop(self.pheap)
            #same priority task can be added to a different user so just check
            #if the current entry is the same as the currently up to date
            if -taskId in self.task_dict and (userId, -p) == self.task_dict[-taskId]:
                self.rmv(-taskId)
                return userId

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()