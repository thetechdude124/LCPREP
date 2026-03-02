class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #the key idea is that you can match like and non-like values
        #for every value, pair it up with another one that's not like itself
        #at the end, whichever value is left MUST be the majority element
        #because the majority when paired with everything else that's not itself, 
        #will have at least one element remaining
        #whenever we've matcehd the current amount seen just take the next one
        major_val = None
        amount_to_match = 0
        for i in range(len(nums)):
            n = nums[i]
            if amount_to_match == 0:
                amount_to_match += 1
                major_val = n
            else:
                if n == major_val: amount_to_match += 1
                else: amount_to_match -= 1

        return major_val



        