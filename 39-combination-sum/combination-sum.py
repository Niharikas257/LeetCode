class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res  =[]
        path = []
        candidates.sort()
        # sum = 0
        def backtrack(i, total):
            if total == target:
                res.append(path.copy())
                return
            for j in range(i,len(candidates)):
                if total + candidates[j] > target:
                    break
                path.append(candidates[j])
                backtrack(j,total + candidates[j])
                path.pop()
        backtrack(0,0)
        return res


