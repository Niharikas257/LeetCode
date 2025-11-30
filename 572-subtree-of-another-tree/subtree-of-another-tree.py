# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. if we find the element in the tree, we can start recursion from that point, we go to the left and compare the values, if they stop matching at a point, we return false
        # 2. The only question is, how to find that one commom point to start?
        # 3. we start from the root, traverse left and right side and when we find that point, we start another recursion

        def isSame(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if isSame(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

 

