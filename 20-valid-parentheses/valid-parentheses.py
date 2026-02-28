from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        
        #needs to be both a matched paren sequence
        #but parens also need to be of the same type
        #keep a stack of the currently open paranetheses types
        #and make sure that unmatching them works
        #also make sure that the running sum never goes negative
        stack = deque()
        count = 0
        for br in s:
            if count < 0: return False
            if br == "(" or br == "{" or br == "[":
                stack.append(br)
                count += 1
            else: 
                if stack: compBr = stack.pop()
                else: return False
                if compBr == "(" and br != ")": return False
                elif compBr == "[" and br != "]": return False
                elif compBr == "{" and br != "}": return False
                count -= 1
        
        if count == 0: return True
        return False
