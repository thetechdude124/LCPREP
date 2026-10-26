"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        '''

        iterate through the list and create a new node object for each .next, storing pointers
        to the new object in a set
        then iterate through the new linked list and for whatever is specified in random, point it to the
        corresponding address specified in the new list
        basically we will store a mapping from old addr -> new addr to help us determine what the random 
        nodes should point to
        need to create new nodes first for the entire list before processing random since it can point to
        nodes that are out of order w.r.t the correct linear ordering of the linked list

        '''

        oldNewMap = {None : None}

        prevNode = None
        currNode = head
        newHead = None
        while currNode != None:
            # create new node obj
            # the next ptr is just a placeholder
            newCurrNode = Node(currNode.val, currNode.next, currNode.random)

            if newHead == None: newHead = newCurrNode
            if prevNode != None: prevNode.next = newCurrNode

            oldNewMap[currNode] = newCurrNode
            prevNode = newCurrNode
            currNode = currNode.next

        
        # iterate through the linked list and just set the random pointers this time
        currNode = newHead
        while currNode != None:
            currNode.random = oldNewMap[currNode.random]
            currNode = currNode.next
        
        return newHead
