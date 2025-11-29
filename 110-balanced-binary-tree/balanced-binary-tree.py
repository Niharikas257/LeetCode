# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 1. dfs
        # 2. recursion
        # 3. stack - iterative
        # 4. define a function and keep calling dfs(node.left) and dfs(node.right)
        # 5. each step we find the absolute difference of left and right
        #     if more than 1 - false
        #     else true
            
        def dfs(node):
            if node is None:
                return True
            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            
            if abs(right_height - left_height) >1:
                return -1

            return max(left_height, right_height) + 1
        
        return dfs(root) != -1
        