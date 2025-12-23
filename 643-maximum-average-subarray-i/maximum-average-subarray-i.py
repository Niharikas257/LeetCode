class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum / k


#-------------------PREFIX SUM METHOD-------


        n = len(nums)
        pre = [0] * (n + 1)

        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]

        max_sum = float('-inf')
        for i in range(0, n - k + 1):
            curr_sum = pre[i + k] - pre[i]
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum / k

