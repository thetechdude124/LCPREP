class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #Very cool problem! 
        #WHENEVER GIVEN TWO ARRAYS, ALWAYS CHECK TO MAKE SURE IF WE CAN FIND ANY INFORMATION
        #ABOUT THE SECOND ARRAY FROM THE FIRST ARRAY
        #IN THIS CASE IF WE FIX A PIVOT IN THE FIRST ARRAY, WE KNOW EXACTLY WHERE THE 
        #PIVOT FOR THE SECOND ONE IS GOING TO BE
        #AND WE JUST NEED TO MAKE SURE THAT BOTH ARE ON THE SAME SIDE 
        #AS IN, THE FRST HALF OF ARR2 IS LESS THAN THE SECOND HALF OF ARR1 (SO LHS)
        #AND THE FIRST HALF OF THE FIRST ARRAY IS LESS THAN THE SECOND HALF OF ARR2
        #MEANING THAT IT IS A VALID PARTITION

        if nums1 == []:
            mid = len(nums2)//2
            if len(nums2) % 2 == 0: 
                return (nums2[mid] + nums2[mid-1])/2
            else: return nums2[mid]
        if nums2 == []:
            mid = len(nums1)//2
            if len(nums1) % 2 == 0: 
                return (nums1[mid] + nums1[mid-1])/2
            else: return nums1[mid]

        total = len(nums1) + len(nums2)
        tgt = int(total/2) if total % 2 == 0 else total//2 + 1

        lo = 0
        hi = min(len(nums1), tgt) + 1
        median = None
        while lo < hi:
            i = lo + (hi - lo)//2
            j = tgt - i #j is also the number of elements to include
            #use this as a partition (inclusive)
            arr1Smaller = False
            arr2Smaller = False
            
            #if j is larger than the number of elements in the given array,
            #this target selection is fundamentally invalid
            #need to increase i, so arr2smaller must be false
 
            if i == 0 or j >= len(nums2) or nums1[i - 1] <= nums2[j]: 
                arr1Smaller = True

            if j <= len(nums2) and (j == 0 or i >= len(nums1) or nums2[j - 1] <= nums1[i]):
                arr2Smaller = True
            
            if arr1Smaller and arr2Smaller:
                if i == 0: median = nums2[j-1]
                elif j == 0: median = nums1[i-1]
                else: median = max(nums1[i-1], nums2[j-1])

                if total % 2 == 0:
                    #take the max with the min
                    corr_factor = 0
                    if j >= len(nums2): corr_factor = nums1[i]
                    elif i >= len(nums1): corr_factor = nums2[j]
                    else: corr_factor = min(nums1[i], nums2[j])

                    median = (median + corr_factor)/2
                break
            elif not arr1Smaller:
                hi = i
            elif not arr2Smaller:
                lo = i + 1

        return median
            
