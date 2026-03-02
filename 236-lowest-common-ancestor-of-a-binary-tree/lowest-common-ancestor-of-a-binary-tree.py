# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def mergeLCAs(root, p, q):

            if root == p or root == q or root == None: return root

            rightres = mergeLCAs(root.right, p, q)
            leftres = mergeLCAs(root.left, p, q)
            if rightres != None and leftres != None:
                return root
            elif rightres != None: return rightres
            else: return leftres


        return mergeLCAs(root, p, q)

