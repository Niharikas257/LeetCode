# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                # If there is no root, then the tree is empty and it has to be balanced with height zero, so it returns true for balanced root and 0 for height.
                return [True, 0]
            
            left = dfs(root.left)
            # left and right variables will store the return value of the dfs, so left[0] tells if the particular subtree/tree is balanced and left[1] tells the height returned by the dfs function
            right = dfs(root.right)
            # balanced is a boolean value to store true or false
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <=1
            return(balanced, 1+ max(left[1], right[1]))
        
        return dfs(root)[0]


        