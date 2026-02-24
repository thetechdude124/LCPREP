class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo = 1
        hi = max(piles) + 1 #exclusive bound
        ans = -1
        while lo < hi:
            k = lo + (hi - lo)//2

            #determine if, given a candidate value of k, we can satisfy the number of piles
            #given the appropriate number of hours
            def determine_if_fit(k : int):
                n_hours_required = 0
                for pile in piles:
                    if pile < k: 
                        n_hours_required += 1
                    else: 
                        n_hours_required += pile // k
                        if pile % k != 0: 
                            n_hours_required += 1
                    if n_hours_required > h: 
                        return False
                return True
            
            if determine_if_fit(k): 
                hi = k
                ans = k
            else:
                lo = k + 1
        return ans

                

        