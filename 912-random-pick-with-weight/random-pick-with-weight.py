import random
class Solution:

    def __init__(self, w: List[int]):
        self.warr = w + [float('inf')]
        self.wsum = sum(w)
        
    def pickIndex(self) -> int:

        #first, generate a random integer from 1 -> total sum
        #depending on where it falls, yield a given index
        #in other words, uniform distribution with different partitions for 
        #different events
        rand_int = random.randint(1, self.wsum)
        prev_w = 1
        for i, w in enumerate(self.warr):
            if prev_w <= rand_int and prev_w + w > rand_int:
                return i
            prev_w += w

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()