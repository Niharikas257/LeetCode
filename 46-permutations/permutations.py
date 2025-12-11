class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # path = []
        # used = [False]*len(nums)
        # def backtrack():
        #     if len(path) == len(nums):
        #         res.append(path.copy())
        #         return 

        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
        #         path.append(nums[i])
        #         used[i] = True
        #         backtrack()
        #         path.pop()
        #         used[i] = False
        # backtrack()
        # return res

        res = []
        path = []
        visited = set()
        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                dfs()
                path.pop()
                visited.remove(nums[i])
        
        dfs()
        return res
            

        
