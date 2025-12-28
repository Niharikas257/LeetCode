class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # answer1 = 0
        # answer2 = 0
        # for num in nums1:
        #     if num in nums2:
        #         answer1 += 1
        # for num in nums2:
        #     if num in nums1:
        #         answer2 +=1 
        # return [answer1, answer2]

#---------Using extra space-------------------#

        # nums1_hash = {}
        # for num in nums1:
        #     nums1_hash[num] = nums1_hash.get(num, 0) + 1

        # nums2_hash = {}
        # for num in nums2:
        #     nums2_hash[num] = nums2_hash.get(num, 0) + 1

        # answer1, answer2  = 0, 0

        # for num in nums1:
        #     if num in nums2_hash:
        #         answer1 +=1 
        # for num in nums2:
        #     if num in nums1_hash:
        #         answer2 += 1
        # return [answer1, answer2]

#-------------sorting the array ----------------#

        nums1.sort()
        nums2.sort()
        i = 0
        j = 0

        answer1 = 0
        answer2 = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                v = nums1[i]

                c1 = 0
                while i < len(nums1) and nums1[i] == v:
                    # if num == v:
                    c1 +=1 
                    i +=1 
                c2 = 0
                while j < len(nums2) and nums2[j] == v:
                    # if num == v:
                    c2 += 1
                    j += 1
                answer1 += c1
                answer2 += c2

            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return [answer1, answer2]
                

                


        



            

        