class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # def dfs(i, subset, total):
        #     if total == target:
        #         res.append(subset.copy())
        #         return
        #     if i >= len(candidates) or total > target:
        #         return
        #     subset.append(candidates[i]) # This loop will keep on adding the same number again and again until either the number becomes greater than target or equal to it.
        #     dfs(i, subset,total+candidates[i])
        #     subset.pop()
        #     dfs(i+1, subset, total)
        # dfs(0,[],0)
        # return res
        res = []
        subset= []
        def dfs(i, subset, total):
            if total==target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            subset.append(candidates[i])
            dfs(i, subset, total+candidates[i])
            subset.pop()
            dfs(i+1, subset, total)
        dfs(0, [],0)
        return res

