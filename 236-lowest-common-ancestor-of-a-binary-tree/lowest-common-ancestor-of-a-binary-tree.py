# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        '''
        General idea: find p and q recursively
        the first subtree that has both p and q, add its root, and thats the LCA

        '''

        def lcaFind(root):
            if root is None or root == p or root == q: return root

            foundLeft  = lcaFind(root.left)
            foundRight  = lcaFind(root.right)

            if foundLeft != None and foundRight != None: return root
            if foundLeft == None: return foundRight
            return foundLeft

        return lcaFind(root)






        # def mergeLCAs(root, p, q):

        #     if root == p or root == q or root == None: return root

        #     rightres = mergeLCAs(root.right, p, q)
        #     leftres = mergeLCAs(root.left, p, q)
        #     if rightres != None and leftres != None:
        #         return root
        #     elif rightres != None: return rightres
        #     else: return leftres


        # return mergeLCAs(root, p, q)

