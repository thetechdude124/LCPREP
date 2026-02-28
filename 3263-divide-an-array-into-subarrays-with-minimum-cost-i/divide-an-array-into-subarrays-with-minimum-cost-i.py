import heapq

class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        #ALWAYS SEE WHAT KEY RESTRICTIONS THE PROBLEM HAS
        #IF THE START IS THE COST, THEN THE FIRST ELEMENT IS ALWAYS INVOLVED

        #store arr elements and their indexes in the heap
        #retrieve 2 smallest ones and sum them up
        #so we just want the sum of the three smallest elements in the array
        #that we can draw the given partitions around
        smallest_elements = []
        for i, num in enumerate(nums):
            if i == 0: continue
            heapq.heappush(smallest_elements, num)
        #get the top 2 elements (not starting at the first)
        
        top_2 = []
        for i in range(2):
            top_2.append(heapq.heappop(smallest_elements))

        s = nums[0]
        for val in top_2:
            s += val
        return s
        