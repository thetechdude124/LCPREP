from bisect import bisect_left, bisect_right

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:

        # sort the given list, then use bisect left
        #gives us the starting index after which all lexicographical prefixes can occur
        # then just walk up until we get there
        suggestedProds = []
        sortedProds = sorted(products) #O(n log n)

        word = ""
        for char in searchWord:
            word += char
            idxBefore = bisect_left(sortedProds, word)
            recs = []
            
            for i in range(3):
                if idxBefore + i >= len(sortedProds): break
                candidate = sortedProds[idxBefore + i]
                if candidate.startswith(word):
                    recs.append(candidate)
            suggestedProds.append(recs)

        return suggestedProds

