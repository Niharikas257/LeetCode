# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        def dfs(node, running_sum):
            if node is None:
                return 0
            running_sum += node.val
            
            needed = running_sum - targetSum
            total = prefix_count[needed]

            prefix_count[running_sum] += 1

            total += dfs(node.left, running_sum)
            total += dfs(node.right, running_sum)

            prefix_count[running_sum] -= 1
            return total
        return dfs(root, 0)



            

        
        