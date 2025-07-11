class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i>=len(nums):
                res.append(subset.copy()) # after the end of every loop, the subset is getting popped and if we are not using copy then every line of code is directing to the same subset from which we are popping at the end of the loop, which is empty.So, the code will run the required number of times, but it will always append empty subset/ popped subset.
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return res
