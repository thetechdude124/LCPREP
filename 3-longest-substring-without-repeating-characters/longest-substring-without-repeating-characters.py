class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #start it at the last moment we saw the char + 1

        #BETTER IDEA -> JUST USE THE SUFFIX!
        #I.E. TRACK THE STRING YOU'VE SEEN SO FAR, AND THEN WHEN YOU SEE A DUPLICATE,
        #CHOP OFF THE PREFIX SEEN!
        #There's no need to scan what we've already seen lol, just use the result
        #again, whenever one sees a repeated use of computation is when optimizations can be introduced 

        seenVals = {}
        maxLenFound = 0
        currLen = 0
        startPtr = 0
        currIdx = 0
        
        while currIdx < len(s):
            c = s[currIdx]
            if c not in seenVals:
                currLen += 1
                seenVals[c] = currIdx
                currIdx += 1
            else:
                newStart = seenVals[c] + 1
                #remove everything from startPtr -> seenVals[c] (where the current prefix is)
                for i in range(startPtr, newStart):
                    del seenVals[s[i]]
                maxLenFound = max(maxLenFound, currLen)
                currLen -= newStart - startPtr
                startPtr = newStart
                
                #now add the current char to the dictionary
                currLen += 1
                seenVals[c] = currIdx
                currIdx += 1

            if currIdx >= len(s) - 1:
                maxLenFound = max(maxLenFound, currLen)
        return maxLenFound

                

        # while currIdx < len(s):
        #     c = s[currIdx]
        #     if c not in currFound: 
        #         currFound[c] = currIdx
        #         currLen += 1
        #         currIdx += 1
        #     else:
        #         maxLenFound = max(currLen, maxLenFound)
        #         currIdx = currFound[c] + 1
        #         currLen = 0
        #         currFound = {}
        #     if currIdx >= len(s) - 1:
        #         maxLenFound = max(currLen, maxLenFound)

        # return maxLenFound
