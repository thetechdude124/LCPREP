import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        #make hash for the indexes corresponding to every number
        self.num_idxs = {}
        for i, num in enumerate(nums):
            if num not in self.num_idxs:
                self.num_idxs[num] = [i]
            else:
                #since we're going from L->R this ensures the 
                #i's are in sorted order
                self.num_idxs[num].append(i)
        

    def pick(self, target: int) -> int:
        idxs = self.num_idxs[target]
        if len(idxs):
            idx = random.randint(0, len(idxs) - 1)
            return idxs[idx]
        return idxs[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)