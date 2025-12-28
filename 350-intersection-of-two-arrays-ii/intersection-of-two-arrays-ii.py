class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash = {}
        for num in nums1:
            nums1_hash[num] = nums1_hash.get(num, 0) + 1
        
        nums2_hash = {}
        for num in nums2:
            nums2_hash[num] = nums2_hash.get(num, 0) + 1

        arr = []
        for num, c1 in nums1_hash.items():
            if num in nums2_hash:
                c2 = nums2_hash[num]
                arr.extend([num] * min(c1, c2))
        return arr