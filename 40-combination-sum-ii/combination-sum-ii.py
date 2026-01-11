class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # path = []
        # candidates.sort()

        # def dfs(index, total):
        #     if total == target:
        #         res.append(path.copy())
        #         return 
        #     for i in range(index, len(candidates)):
        #         if i > index and candidates[i] == candidates[i-1]:
        #             continue
        #         if total + candidates[i]> target:
        #             return
        #         path.append(candidates[i])
        #         dfs(i+1, total + candidates[i])
        #         path.pop()
        # dfs(0,0)
        # return res

        res = []
        path = []
        candidates.sort()

        def dfs(index, total):
            if total == target:
                res.append(path.copy())
            
            for i in range(index, len(candidates)):
                if total > target:
                    return
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                dfs(i+1, candidates[i]+total)
                path.pop()
        dfs(0,0)
        return res

