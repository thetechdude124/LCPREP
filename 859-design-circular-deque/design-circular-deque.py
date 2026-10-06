class MyCircularDeque:

    def __init__(self, k: int):
        self.buf = [0] * k
        self.head = 1 #on the very first iter make the head at the beginning of the array
        #don't actually need to do this but i find it cleaner; works cause k >= 1
        self.k = k
        self.size = 0


    def insertFront(self, value: int) -> bool:
        if self.size == self.k: return False
        # get idx just before head mod k
        newhead = (self.head - 1) % self.k #if negative just wraps around
        self.head = newhead
        self.size += 1
        self.buf[self.head] = value
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.size == self.k: return False
        last_idx = (self.head + self.size) % self.k
        self.buf[last_idx] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0: return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.size == 0: return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0: return -1
        return self.buf[self.head]

    def getRear(self) -> int:
        if self.size == 0: return -1
        last_idx = (self.head + self.size - 1) % self.k
        return self.buf[last_idx]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()