# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        l = []
        
        def checkBST(root):
            if root:
                checkBST(root.left)
                l.append(root.val)
                checkBST(root.right)
            
        checkBST(root)
        
        if len(l) != len(set(l)):
            return False
        
        if l == sorted(l):
            return True
        else:
            return False