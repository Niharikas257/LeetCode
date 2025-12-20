class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        count = Counter(nums)
        ans = 0
     
        if k ==0: 
            for freq in count.values():
                if freq >=2:
                    ans += 1
            
        else:
            for num in count:
                if num+k in count:
                    ans += 1
            
        return ans



