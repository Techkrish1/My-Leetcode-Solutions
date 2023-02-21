# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBST(self, preorder, maxVal):
        if not preorder or preorder[-1] > maxVal:
            return None
        root = TreeNode(preorder.pop())
        root.left = self.createBST(preorder, root.val)
        root.right = self.createBST(preorder, maxVal)
        return root
    
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.createBST(preorder[::-1], sys.maxsize)