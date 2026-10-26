# node class
class Node: 
    def __init__(self, key = None, data = None):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

'''
[head, a, b, tail]


'''
# doubly linked list class
class DoublyLinkedList:

    def __init__(self):

        # sentinel head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.len = 0

    # to remove an element from the tail of the list (because this will be our 
    # least recently used element)
    def removeTail(self):
        if self.len > 0:
            self.len -= 1

            left = self.tail.prev.prev
            curr = self.tail.prev
            left.next = self.tail
            self.tail.prev = left

            return curr #need to know which node we just removed
        return None

    def removeNode(self, node):
        self.len -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        # so that python will garbadge collect it
        node.next = None
        node.prev = None

    # adds node to the head of the list
    def addNode(self, node):
        self.len += 1

        # set the pointers of node first
        node.next = self.head.next
        node.prev = self.head

        # then adjust the pointers of everything else
        self.head.next.prev = node
        self.head.next = node

class LRUCache:

    def __init__(self, capacity: int):
        
        # overall strategy: have a dictionary that maps the keys we're looking up 
        # to the data
        # this is so that get is O(1)
        self.keyToNode = {}
        self.cache = DoublyLinkedList()
        self.c = capacity

    def get(self, key: int) -> int:

        if key not in self.keyToNode: return -1
        
        # remove node from current position and add to the front of the linked list
        node = self.keyToNode[key]
        self.cache.removeNode(node)
        self.cache.addNode(node)

        return node.data

    def put(self, key: int, value: int) -> None:
        
        # key exists
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.data = value

            # update position
            self.cache.removeNode(node)
            self.cache.addNode(node)

        else:
            
            newNode = Node(key, value)
            self.cache.addNode(newNode)
            self.keyToNode[key] = newNode

            # if we've exceeded capacity then remove the tail
            if self.cache.len > self.c:
                removedNode = self.cache.removeTail()
                del self.keyToNode[removedNode.key] 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)