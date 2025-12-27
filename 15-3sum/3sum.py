class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res :set[Tuple[int, int, int]] = set()
        used_a: set[int] = set()
        n = len(nums)
        for i in range(len(nums)):
            a = nums[i]
            if a in used_a:
                continue
            used_a.add(a)

            seen: set[int] = set()
            for j in range(i+1, n):
                b = nums[j]
                c = -a-b

                if c in seen:
                    res.add(tuple(sorted((a,b,c))))
                seen.add(b)
        return [list(t) for t in res]


#--------------------------------------------------------#
        # nums.sort()
        # res = []

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] > 0:
        #         break
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
            
        #     left = i+1
        #     right = len(nums) - 1
        #     while left < right:
        #         three_sum = nums[i] + nums[left] + nums[right]
        #         if three_sum > 0:
        #             right -= 1
        #         elif three_sum < 0:
        #             left +=1
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left-1]:
        #                 left += 1
        #             # while left < right and nums[right] == nums[right + 1]:
        #             #     right -= 1
        # return res





            
