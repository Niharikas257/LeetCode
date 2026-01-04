# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result: List[List[int]] = []

        # def dfs(node: Optional['TreeNode'], cur_sum: int, path: List[int]) -> None:
        #     if not node:
        #         return 
        #     cur_sum = cur_sum + node.val
        #     path.append(node.val)
        #     if node.left is None and node.right is None:
        #         if cur_sum == targetSum:
        #             result.append(list(path))
        #     else:
        #         dfs(node.left, cur_sum, path)
        #         dfs(node.right, cur_sum, path)
            
        #     path.pop()
        
        # if root is None:
        #     return result
        # dfs(root, 0,[])
        # return result

       
        def dfs(node, cur_sum, path):
            if node is None:
                return 
            cur_sum += node.val
            path.append(node.val)
            if node.left is None and node.right is None:
                if cur_sum == targetSum:
                    result.append(list(path))
                    # return result
            else:
                dfs(node.left, cur_sum, path)
                dfs(node.right, cur_sum, path)

            path.pop()
        dfs(root, 0, [])
        return result
        