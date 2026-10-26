from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        if root == None: return []
        levels = []
        q = deque([(root, 0)])
        visited = set()

        while q:
            node, level = q.popleft()
            visited.add(node)
            levels.append([node, level])
            for nbor in [node.left, node.right]:
                if nbor is not None and nbor not in visited:
                    q.append((nbor, level + 1))

        nested_levels = []
        prev_level = -1
        curr_level = []
        for node, level in levels + [(None, -2)]:
            if level != prev_level:
                prev_level = level
                nested_levels.append(curr_level)
                if node != None: curr_level = [node.val]
                else: curr_level = [node]
            else:
                curr_level.append(node.val)
        
        # add the last node in separately
        return nested_levels[1:]
        
                
