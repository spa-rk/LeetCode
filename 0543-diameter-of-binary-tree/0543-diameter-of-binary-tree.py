# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_res = 0

        def height(root):
            nonlocal max_res
            
            if root == None:
                return -1
            
            left_h = height(root.left)
            right_h = height(root.right)
            
            max_res = max(max_res, (left_h + 1) + (right_h + 1) )
            
            return max(left_h, right_h) + 1
            
        height(root)
        
        return max_res