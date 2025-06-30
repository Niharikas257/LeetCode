# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # Changed to return True for empty tree
        stack = [(root, float('-inf'), float('inf'))]  # Track (node, lower bound, upper bound)
        
        while stack:
            node, low, high = stack.pop()  # Unpack node, low, high
            
            if not (low < node.val < high):  # Check if node value is within the valid range
                return False

            if node.right:
                stack.append((node.right, node.val, high))  # Update lower bound for right child
            if node.left:
                stack.append((node.left, low, node.val))  # Update upper bound for left child

        return True  # Return True if all nodes are valid
