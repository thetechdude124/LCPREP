class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #option one -> just convert to string, check if its equal to its reverse
        return str(x) == str(x)[::-1]