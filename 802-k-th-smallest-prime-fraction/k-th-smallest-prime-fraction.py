from typing import List, Tuple

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def isValid(x: float) -> Tuple[int, int, int]:
            i = -1
            count = 0
            best_num = 0
            best_den = 1

            for j in range(1, len(arr)):
                while i + 1 < j and arr[i + 1] <= x * arr[j]:
                    i += 1

                count += (i + 1)

                if i >= 0 and best_num * arr[j] < arr[i] * best_den:
                    best_num, best_den = arr[i], arr[j]

            return count, best_num, best_den

        low, high = 0.0, 1.0
        ans = [0, 1]

        for _ in range(60):
            mid = (low + high) / 2.0
            count, best_num, best_den = isValid(mid)

            if count < k:
                low = mid
            else:
                high = mid
                ans = [best_num, best_den]

        return ans
