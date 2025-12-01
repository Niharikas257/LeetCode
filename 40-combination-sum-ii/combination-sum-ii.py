class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(j, total):
            if total == target:
                res.append(path.copy())
                # print(path.copy())
                return
            
            for i in range(j, len(candidates)):
                if i > j and candidates[i] == candidates[i-1]:
                    continue
                
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, candidates[i] + total)
                path.pop()


        backtrack(0,0)
        return res

