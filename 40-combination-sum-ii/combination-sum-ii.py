class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # path = []
        # candidates.sort()

        # def backtrack(i, total):
        #     if total == target:
        #         res.append(path.copy())
        #         return res
        #     for j in range(i, len(candidates)):

        #         if j > i and candidates[j] == candidates[j-1]:
        #             continue
        #         if candidates[j] + total > target:
        #             break
        #         path.append(candidates[j])
        #         backtrack(j+1, total + candidates[j])
        #         path.pop()
        
        # backtrack(0,0)
        # return res
##############
        res = []
        path = []
        candidates.sort()

        def dfs(index, total):
            if total == target:
                res.append(path.copy())
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i]> target:
                    return
                path.append(candidates[i])
                dfs(i+1, total + candidates[i])
                path.pop()
        dfs(0,0)
        return res

