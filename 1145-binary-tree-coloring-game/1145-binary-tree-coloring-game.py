# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        opp = None
        
        def DFS(root):
            if root == None:
                return 0
            
            nonlocal x
            if root.val == x:
                nonlocal opp
                opp = root
                return 0
            
            return 1 + DFS(root.left) + DFS(root.right)
        
        above = DFS(root)
        left = DFS(opp.left)
        right = DFS(opp.right)
        
        if (above > left + right) or (left > above + right) or (right > above + left):
            return True
        
        return False