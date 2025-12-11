class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # path = []

        # def backtrack(k):
        #     res.append(path[:])
        #     for i in range(k, len(nums)):
        #         path.append(nums[i])
        #         backtrack(i+1)
        #         path.pop()
        # backtrack(0)
        # return res

        res = []
        path = []

        def dfs(index, path):
            if index == len(nums):
                res.append(path.copy())
                return
            
            dfs(index+1, path)
            path.append(nums[index])
            dfs(index+1, path)
            path.pop()

        dfs(0,[])
        return res

