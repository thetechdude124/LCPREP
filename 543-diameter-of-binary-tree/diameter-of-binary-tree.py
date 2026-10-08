# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxSeen = [0]
        def getDiameter(node, maxSeen):
            
            if node == None: return 0

            maxDepthLeft = getDiameter(node.left, maxSeen)
            maxDepthRight = getDiameter(node.right, maxSeen)

            newMax = maxDepthLeft + maxDepthRight
            maxSeen[0] = max(maxSeen[0], newMax)

            return max(maxDepthLeft, maxDepthRight) + 1


        getDiameter(root, maxSeen)
        return maxSeen[0]