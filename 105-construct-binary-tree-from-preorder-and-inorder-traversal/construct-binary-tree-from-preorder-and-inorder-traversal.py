# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Because we need to construct a binary tree, so we have to create the object of the class TreeNode, otherwise, it would just be a variable.
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        # we need to find mid because in inorder traversal, left and right are divided by the root which we already have
        mid = inorder.index(preorder[0]) # this finds the index in the inorder which has the same value as the root, which is in the middle of the inrder.
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
    
    

        