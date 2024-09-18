class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        
        # Ensure that A is the smaller array to optimize binary search
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2  # Midpoint in A
            j = half - i - 2  # Corresponding position in B
            
            # Edge case handling for out-of-bounds
            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Correct partition found
            if A_left <= B_right and B_left <= A_right:
                # If odd total, return the middle element
                if total % 2:
                    return min(A_right, B_right)
                # If even total, return the average of the middle elements
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            # Adjust the binary search range
            elif A_left > B_right:
                r = i - 1  # Move partition A to the left
            else:
                l = i + 1  # Move partition A to the right
































# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         A = nums1
#         B = nums2
        
#         if len(B) < len(A):
#             A,B = B,A
            
#         total = len(A)+len(B)
#         half = total // 2
        
#         l = 0
#         r = len(A)-1
        
#         # We are starting the loop before initializing the i and j value because we might need to update i if           # the partition is not correct.
#         while True:
#             i = (l+r)//2
#             j = half - i - 2
            
#             A_left = A[i] if i >= 0 else float("-infinity")
#             A_right = A[i+1] if (i+1) < len(A) else float("infinity")
#             B_left = B[j] if j>=0 else float("-infinity")
#             B_right = B[j+1] if j < len(B) else float("infinity")      
            
#             if A_left<= B_right and A_right >= B_left:
#                 if total%2: # means if the total is odd, because in that case it will return 1 (True)
#                     return min(A_right, B_right)
#                 else:
#                     return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
                
#             elif A_left > B_right:
#                 i = i-1
            
#             else:
#                 i = i+1
                
                    
        
        