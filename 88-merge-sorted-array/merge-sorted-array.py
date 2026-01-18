class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1_read = m-1
        # nums2_read = n-1
        # write = m+n-1

        # while nums2_read >= 0:
        #     if nums1_read >= 0 and nums1[nums1_read] > nums2[nums2_read]:
        #         nums1[write] = nums1[nums1_read]
        #         nums1_read -= 1
        #     else:
        #         nums1[write] = nums2[nums2_read]
        #         nums2_read -= 1
        #     write -= 1

            
        i = m-1
        j = n-1
        write = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
        while j >= 0:
            nums1[write] = nums2[j]
            j -= 1
            write -= 1

