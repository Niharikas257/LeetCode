class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1_hash = {}
        # for num in nums1:
        #     nums1_hash[num] = nums1_hash.get(num, 0) + 1
        
        # nums2_hash = {}
        # for num in nums2:
        #     nums2_hash[num] = nums2_hash.get(num, 0) + 1

        # arr = []
        # for num, c1 in nums1_hash.items():
        #     if num in nums2_hash:
        #         c2 = nums2_hash[num]
        #         arr.extend([num] * min(c1, c2))
        # return arr        
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

