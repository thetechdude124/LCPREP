class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #for every pair of larger side and smaller side, moving the larger
        #side has no further effect (assuming that the width is at max) so 
        #only possible gains can come from moving the smaller side
        
        p1 = 0
        p2 = len(height) - 1
        maxRes = float("-inf")

        while p1 != p2:
            consideredHeight = min(height[p1], height[p2])
            maxRes = max(maxRes, consideredHeight * (p2 - p1))
            if height[p1] < height[p2]:
                p1 += 1
            elif height[p2] < height[p1]:
                p2 -= 1
            else: p1 += 1
        return maxRes

        
