class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()

        def dfs(index, total):
            if total == target:
                res.append(path.copy())
            
            for i in range(index, len(candidates)):
                if total > target:
                    return
                path.append(candidates[i])
                dfs(i, candidates[i] + total)
                path.pop()
        dfs(0,0)
        return res
        