class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # visited = set()
        path = []

        def backtrack(i):
            res.append(path[:])
            for i in range(i, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return res
                

