class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # path = []

        # def dfs(index, path):
        #     res.append(path.copy())
        #     for i in range(index, len(nums)):
        #     # dfs(index+1, path) # Skip
        #         path.append(nums[i]) # Take
        #         dfs(i+1, path)
        #         path.pop() # clean it for future

        # dfs(0,[])
        # return res

        path = []
        res = []
        def dfs(index, path):
            res.append(path.copy())
            for i in range(index, len(nums)):
                # if i < len(nums) and nums[i] == nums[i-1]:
                #     continue
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0,[])
        return res


