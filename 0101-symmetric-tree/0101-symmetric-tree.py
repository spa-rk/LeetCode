# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack, left, right = [], root.left, root.right
        while stack or left and right:
            if not (left or right):
                right = stack.pop().left
                left = stack.pop().right
            elif not left or not right or left.val != right.val:
                return False
            else:
                stack.append(left)
                stack.append(right)
                left, right = left.left, right.right

        return not (stack or left or right)        