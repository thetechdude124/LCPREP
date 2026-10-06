import heapq
from itertools import count

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        if lists == None: return None

        '''

        Core invariant: at any given point, we just want to choose the smallest
        elemnet from the k queues (since each linked list is sorted, we guarantee
        that the next smallest elemnet must be the min(head of each queue)). 
        
        At each timestep to figure out the smallest element to add we can just use a 
        heap of maxsize k, and then push the next element from the queue whose element
        we just took

        time complexity: O(n log k) space complexity: O(k)

        '''   

        counter = count()

        #remove all zero element lists
        filtered = [x for x in lists if x != None]
        next_element_heap = []

        # place first k elements in heap
        for node in filtered:
            # counter is incremented so that we don't use incomprable node obj 
            # to break ties
            heapq.heappush(next_element_heap, (node.val, next(counter), node))

        currNode = None
        firstNode = None
        first_iter = True

        while len(next_element_heap) > 0:
            #pop next element from the heap and attach to current node
            _, _, nextNode = heapq.heappop(next_element_heap)
            #push next val from that sequence into the heap if not none
            if nextNode.next != None:
                heapq.heappush(next_element_heap, (nextNode.next.val, next(counter), nextNode.next))

            if first_iter: 
                currNode = nextNode
                firstNode = currNode
                first_iter = not first_iter
            else: currNode.next = nextNode
            currNode = nextNode

        return firstNode


            
