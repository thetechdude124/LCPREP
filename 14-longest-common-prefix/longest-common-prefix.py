class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #better idea
        #first, get the smallest possible word
        #then just check if that word lines up with the others and if so how much
        #if no alignment with some word can just do early termination
        smallest_word = None
        min_len_found = float('inf')
        for s in strs:
            if len(s) < min_len_found:
                min_len_found = len(s)
                smallest_word = s
        
        candidate_prefix = list(smallest_word)
        for s in strs:

            if len(s) < len(candidate_prefix):
                candidate_prefix = candidate_prefix[:len(s)]

            for j in range(len(candidate_prefix)):
                if candidate_prefix[j] != s[j]:
                    candidate_prefix = candidate_prefix[:j]
                    if candidate_prefix == []: return ""
                    break
        return "".join(candidate_prefix)
