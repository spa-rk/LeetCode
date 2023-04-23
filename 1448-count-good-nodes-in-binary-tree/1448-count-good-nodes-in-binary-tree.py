# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [0]
        self.get_good_nodes(root, good_nodes, root.val)
        
        return good_nodes[0]
    
    def get_good_nodes(self, root: TreeNode, good_nodes: List[int], cur_max) -> int:
        if not root:
            return
        
        if root.val >= cur_max:
            good_nodes[0] += 1
            cur_max = root.val
        
        self.get_good_nodes(root.left, good_nodes, cur_max)
        self.get_good_nodes(root.right, good_nodes, cur_max)
        