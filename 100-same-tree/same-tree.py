# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p is None and q is None:
    #         return True
    #     if p is None or q is None:
    #         return False
    #     def bfs(node):
    #         q = deque()
    #         q.append(node)
    #         res = []
    #         while q:
    #             cur = q.popleft()
    #             if cur is None:
    #                 res.append(None)
    #                 continue
    #             res.append(cur.val)
    #             if cur.left:
    #                 q.append(cur.left)
    #             if cur.left is None:
    #                 q.append(None)
    #             if cur.right:
    #                 q.append(cur.right)
    #             if cur.right is None:
    #                 q.append(None)
    #         return res
    #     res_p = bfs(p)
    #     res_q = bfs(q)
    #     if res_p and res_q and res_p == res_q:
    #         return True
    #     else:
    #         return False

            # How about, we do the traversal and return the res for both and compare that result 

        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            dq = deque([(p,q)])
            while dq:
                a,b = dq.popleft()
                if a is None and b is None:
                    continue
                if a is None or b is None:
                    return False

                if a.val != b.val:
                    return False
                dq.append((a.left, b.left))
                dq.append((a.right, b.right))
            return True



        