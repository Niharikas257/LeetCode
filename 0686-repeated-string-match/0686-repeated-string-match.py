# import math
# class Solution(object):
#     def repeatedStringMatch(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: int
#         """
#         min_repeats = int(math.ceil(len(b)/len(a)))
        
#         if b in a*min_repeats:
#             return min_repeats
#         elif b in a * (min_repeats + 1):  return min_repeats + 1
#         else: return -1

import math

class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # Calculate the minimum number of repeats needed
        min_repeats = int(math.ceil(len(b) / len(a)))

        # Check if b is a substring of repeated a with min_repeats or min_repeats + 1 repeats
        if b in a * min_repeats:
            return min_repeats
        elif b in a * (min_repeats + 1):
            return min_repeats + 1
        elif b in a * (min_repeats + 2):
            return min_repeats + 2

        return -1


