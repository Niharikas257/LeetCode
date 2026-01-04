# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
        if not preorder or not inorder:
            return None

        # Map each value to its index in inorder so we can split left vs right in O(1).
        pos = {}
        for i, value in enumerate(inorder):
            pos[value] = i

        # This pointer always indicates the next root to take from preorder.
        pre_idx = 0

        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            """
            Build the subtree whose inorder slice is inorder[in_left .. in_right].
            """
            nonlocal pre_idx

            # Base case: no elements means no subtree.
            if in_left > in_right:
                return None

            # Preorder gives the root first for this subtree.
            root_val = preorder[pre_idx]
            pre_idx += 1

            # Create the root node.
            root = TreeNode(root_val)

            # Find where this root appears in inorder to split left and right subtrees.
            mid = pos[root_val]

            # Build left subtree from inorder left segment.
            root.left = build(in_left, mid - 1)

            # Build right subtree from inorder right segment.
            root.right = build(mid + 1, in_right)

            return root

        # Build the whole tree using the full inorder range.
        return build(0, len(inorder) - 1)
        
        
        
        # if not preorder or not inorder:
        #     return None
        

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # return root
