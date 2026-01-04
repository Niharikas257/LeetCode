# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root is None:
            return []

        # 1) Build parent pointers so we can move upward like an undirected graph
        parent = {root: None}
        q = deque([root])

        while q:
            node = q.popleft()

            if node.left is not None:
                parent[node.left] = node
                q.append(node.left)

            if node.right is not None:
                parent[node.right] = node
                q.append(node.right)

        # 2) BFS from target for exactly k layers
        q = deque([target])
        seen = {target}
        dist = 0

        while q and dist < k:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()

                # Neighbors in the "undirected" view of the tree
                for nei in (node.left, node.right, parent[node]):
                    if nei is not None and nei not in seen:
                        seen.add(nei)
                        q.append(nei)

            dist += 1

        # 3) Everything left in the queue is exactly distance k
        return [node.val for node in q]
