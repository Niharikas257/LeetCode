class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = set()

        def dfs(index):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                dfs(i)
                path.pop()
                visited.remove(nums[i])
        dfs(0)
        return res

        # Visited is used so we can not use the already used element again in the same set. But we can't move to i+1 because we want to use previous elements also but just not in the same order
            

        
