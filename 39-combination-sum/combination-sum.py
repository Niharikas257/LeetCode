class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(j, total):
            if total == target:
                res.append(path.copy())
            for i in range(j, len(candidates)):
                if total > target:
                    return
                path.append(candidates[i])
                backtrack(i, total + candidates[i])
                path.pop()
        backtrack(0, 0)
        return res





            