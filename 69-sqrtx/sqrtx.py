class Solution:
    def mySqrt(self, x: int) -> int:

        #we can simply do binary search on the values of mid**2
        lo = 0
        hi = x//2 + 2
        ans = 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            res = mid * mid
            if res == x: 
                return mid
            elif res < x:
                ans = mid
                lo = mid + 1
            else: 
                hi = mid
        return ans
        