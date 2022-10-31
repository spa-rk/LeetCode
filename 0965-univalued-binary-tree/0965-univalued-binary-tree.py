# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
		
        queue = []
        prev = root
        queue.append(prev)

        while queue:
            node = queue.pop()

            if node.val != prev.val:
                return False

            prev = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return True