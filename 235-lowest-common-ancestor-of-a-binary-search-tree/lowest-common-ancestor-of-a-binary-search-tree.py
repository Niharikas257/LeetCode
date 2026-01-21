# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root or not p or not q:
        #     return False
        # if max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, q,p)
        # if min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, q,p)
        # return root

        # if not root:
        #     return None
        # parent = {}
        # parent[root] = None
        # stack = [root]
        # while stack:
        #     if not stack:
        #         return None
        #     node = stack.pop()
        #     while node.left is not None and node.left not in parent:
        #         parent[node.left] = node
        #         stack.append(node.left)
        #     while node.right is not None and node.right not in parent:
        #         parent[node.right] = node
        #         stack.append(node.right)
            
        #     ancestors = set()
        #     cur = p
        #     while cur is not None:
        #         ancestors.add(cur)
        #         cur = parent[cur]
            
        #     cur = q
        #     while cur not in ancestors:
        #         cur = parent[cur]

        # return cur

        cur = root
        while cur is not None:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
        return None

