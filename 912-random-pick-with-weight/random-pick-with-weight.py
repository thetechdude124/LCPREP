import random
class Solution:

    def __init__(self, w: List[int]):
        self.warr = w
        self.wsum = sum(w)

        #build prefix sum array initially to get the range the number is in
        #then use the prefix sum array to query a hashmap, where the hashmap
        #will map each prefix sum range to the corresponding index it belongs to
        #or we could just skip that, iterate from 1-> wsum directly, and cache
        #all of the given results in the hashmap

        #actual solution -> just binary search on the pfa to find the appropriate index lol
        self.pfa = [0, self.warr[0]]
        for i in range(1, len(self.warr)):
            self.pfa.append(self.pfa[i] + self.warr[i])

        
    def pickIndex(self) -> int:

        #first, generate a random integer from 1 -> total sum
        #depending on where it falls, yield a given index
        #in other words, uniform distribution with different partitions for 
        #different events
        rand_int = random.randint(0, self.wsum - 1)
        
        #do binary search on what index this maps to
        lo = 1
        hi = len(self.pfa) #exclusive bound
        corr_idx = None

        while lo < hi:
            mid = lo + (hi - lo)//2

            if rand_int < self.pfa[mid] and self.pfa[mid - 1] <= rand_int:
                corr_idx = mid - 1
                break
            elif rand_int >= self.pfa[mid]:
                lo = mid + 1
            else:
                hi = mid

        return corr_idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()