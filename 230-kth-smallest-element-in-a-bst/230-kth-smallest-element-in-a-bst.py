# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative method
        self.arr = []
        self.k = k
        self.smallest(root, self.arr)
        
        return self.arr[-1]
        
    def smallest(self, root, arr):
        if root:
            self.smallest(root.left, arr)
        
            if len(self.arr) < self.k:
                self.arr.append(root.val)
            else:
                return

            self.smallest(root.right, self.arr)