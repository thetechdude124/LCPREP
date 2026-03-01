class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #start it at the last moment we saw the char + 1
        currFound = {}
        maxLenFound = 0
        currLen = 0
        currIdx = 0

        while currIdx < len(s):
            c = s[currIdx]
            if c not in currFound: 
                currFound[c] = currIdx
                currLen += 1
                currIdx += 1
            else:
                maxLenFound = max(currLen, maxLenFound)
                currIdx = currFound[c] + 1
                currLen = 0
                currFound = {}
            if currIdx >= len(s) - 1:
                maxLenFound = max(currLen, maxLenFound)

        return maxLenFound
