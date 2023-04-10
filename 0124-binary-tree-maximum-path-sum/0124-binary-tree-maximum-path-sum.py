# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-float('inf')]
        def recur(root):

            if not root:
                return 0
            
            lsum = recur(root.left)
            rsum = recur(root.right)
            ans[0] = max(ans[0], root.val, root.val + lsum, root.val + rsum, root.val+ lsum+rsum)
            return max(root.val, root.val+lsum,root.val+rsum)
        

        recur(root)
        return ans[0]