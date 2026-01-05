# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # stack = []
        # cur = root
        # res = []
        # first = None
        # second = None
        # if root is None:
        #     return
        # prev = None
        # while stack or cur is not None:
        #     while cur is not None:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     if prev is not None and cur.val < prev.val:
        #         if first is None:
        #             first = prev
        #         second = cur
        #     prev = cur
        #     cur = cur.right
        
        # first.val, second.val = second.val, first.val

        cur = root
        first = None
        second = None
        if root is None:
            return
        prev = None
        while cur is not None:
            if cur.left is None:
                if prev is not None and cur.val < prev.val:
                    if first is None:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                pred = cur.left
                while pred.right is not None and pred.right is not cur:
                    pred = pred.right
                
                if pred.right is None:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    if prev is not None and cur.val < prev.val:
                        if first is None:
                            first = prev
                        second = cur
                    prev = cur
                    cur = cur.right
        if first is not None and second is not None :
            first.val, second.val = second.val, first.val
                

        