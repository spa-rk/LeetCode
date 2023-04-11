# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return "#"
            
            L = dfs(node.left)
            R = dfs(node.right)
            
            return  str(node.val) + "," + L + "," + R
        
        
        return dfs(root)      

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = [int(d) if d != "#" else None for d in data.split(",") ]
        
        def dfs():
            
            
            last = data.pop(0)
            
            if last == None:
                return None
            
            node = TreeNode(last)
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()