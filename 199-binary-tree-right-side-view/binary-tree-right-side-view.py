# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []

        # q = deque()
        # q.append(root)
        # res = []        

        # while q:
        #     Q = len(q)
        #     for i in range(Q):
        #         cur = q.popleft()
        #         if i == Q -1:
        #             res.append(cur.val)
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        # return res

        if not root:
            return []
        q = deque()
        q.append(root)
        visited = set()
        res = []
        while q:
            size = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if i == size-1 :
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
            


        

        