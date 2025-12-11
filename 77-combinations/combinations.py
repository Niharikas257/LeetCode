class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # res = []
        # path = []
        # def dfs(index):
        #     if len(path) == k:
        #         res.append(path.copy())
        #         return res
        #     remaining = k - len(path)
        #     upper_bound = n - remaining + 1

        #     for i in range(index, upper_bound + 1):
        #         path.append(i)
        #         dfs(i+1)
        #         path.pop()
            

        # dfs(1)
        # return res

        res = []
        path = []
        def dfs(index):
            if len(path) == k:
                res.append(path.copy())
                return res
            remaining = k - len(path)
            upper_bound = n - remaining + 1
            for i in range(index, upper_bound + 1): # This code if for pruning
                path.append(i)
                dfs(i+1)
                path.pop()
        dfs(1)
        return res
            


                 
        