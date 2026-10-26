# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        
        '''

        for each node, we need to decide whether to take it or not
        starting or ending of a path should never be negative; otherwise
        can just discard it and increase the value of the total sum that is present

        if our path length is zero, then dont take it
        if path length is k, then we can take either the left or the right child (or the parent)

        dp on the tree
        can't do traditional dp[i][k] => also don't depend on the path length k beacuse it's useless
        here and doesn't actually matter

        Approach: every single path has a peak v, so can partition based on that
        for each v, get the length of max path on the left and the rigth (path that has no bumps, 
        if it has a bump can't conenct it to v lol) and then join
        then take the max across all v. Let the length of this path starting at node k be f(k)

        so our dp array, given a root, needs to be f(left) + v.val + f(right)for each v
        '''

        if root == None: return 0

        maxNonBentPaths = {}
        def maxNonBentPath(node):
            if node == None: 
                maxNonBentPaths[node] = 0
                return 0
            if node.left == None and node.right == None:
                maxNonBentPaths[node] = node.val
                return node.val
            
            # explore left and right branches
            # need to make this -inf because -1 is actually possible
            rightSum = float("-inf")
            leftSum = float("-inf")
            if node.right != None: 
                if node.right in maxNonBentPaths: rightSum = maxNonBentPaths[node.right]
                else: rightSum = maxNonBentPath(node.right)
            if node.left != None: 
                if node.left in maxNonBentPaths: leftSum = maxNonBentPaths[node.left]
                else: leftSum = maxNonBentPath(node.left)

            if rightSum < 0 and leftSum < 0: maxNonBentPaths[node] = node.val
            else: maxNonBentPaths[node] = max(rightSum, leftSum) + node.val
            return maxNonBentPaths[node]

        # then for each peak we need to store the max length
        # traverse the entire tree
        f_v = {}
        def peakPathCalc(node):
            if node == None: 
                f_v[None] = 0
                return

            # if the left or right paths are negative its better to just to take 0 instead of the negative value
            leftVal = max(0, maxNonBentPath(node.left))
            rightVal = max(0, maxNonBentPath(node.right))
            f_v[node] = leftVal + node.val + rightVal
            peakPathCalc(node.right)
            peakPathCalc(node.left)

        peakPathCalc(root)

        bestRes = float("-inf")
        for k, v in f_v.items():
            if k == None: continue
            bestRes = max(bestRes, v)

        return bestRes