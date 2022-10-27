# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = 1
        cur = [root]
        while True:                                                              
            next_nodes = []                                                      
            for leaf in cur:  
                if leaf == None:
                    continue
                left_child = leaf.left                                           
                right_child = leaf.right
                if left_child == None and right_child == None:  
                    return depth    
                next_nodes.append(left_child)                                    
                next_nodes.append(right_child)                                   

            depth += 1                                                      

            cur = next_nodes