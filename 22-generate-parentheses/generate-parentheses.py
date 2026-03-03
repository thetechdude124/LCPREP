class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #pay attention; n is the number of PAIRS, not the number of total parenthesis generated
        n_total = 2 * n
        ALL_RESULTS = []
        def recursivelyGenerateSequence(generated_so_far, n_right, n_left):
            #observe -> we have a valid sequence if at no point 
            #n right is less than n left
            #so, we can do the following -> enforce that n_right goes up to at most n
            #then, this means that once we hit that barrier, we can only add n_left
            #until the sequence is full
            #this guarentees to us that n_left only goes up to n as well
            #so in total we have a) the correct number of parenthesis, and 
            #at no point does n_left exceed n_right -> so by the end nleft == nright
            #and we therefore have a valid, matching sequence pair
            #LISTS ARE MUTABLE; DON'T PASS INTO RECURSIVE CALLS UNLESS YOU WANT A SHARED STATE
            #ALSO LIST.APPEND RETURNS NONE

            if len(generated_so_far) == n_total:
                #And you're APPENDING THE SAME REFERENCE
                #so need to split
                string = "" .join(generated_so_far)
                ALL_RESULTS.append(string)
                return #don't forget the return in the base case
            
            if n_left < n_right:
                generated_so_far.append(")")
                recursivelyGenerateSequence(generated_so_far, n_right, n_left + 1)
                generated_so_far.pop()
            #can only add up to N of the n_right
            #once this hits n, only thing possible is adding more ) brackets
            #we're considering all options by seeing if we can add both a ( and a ) at every timestep
            if n_right < n:
                generated_so_far.append("(")
                recursivelyGenerateSequence(generated_so_far, n_right + 1, n_left )
                generated_so_far.pop()
        
        recursivelyGenerateSequence([], 0, 0)
        return ALL_RESULTS