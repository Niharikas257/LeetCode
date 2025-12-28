class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        n, m = len(version1), len(version2)

        while i < n or j < m:
            # Parse next integer revision from version1
            num1 = 0
            while i < n and version1[i] != '.':
                # Build the integer value digit by digit
                num1 = num1 * 10 + (ord(version1[i]) - ord('0'))
                i += 1

            # Parse next integer revision from version2
            num2 = 0
            while j < m and version2[j] != '.':
                num2 = num2 * 10 + (ord(version2[j]) - ord('0'))
                j += 1

            # Compare current revision values
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1

            # Skip the dot if present and move to the next revision
            i += 1  # safe even if i == n (no-op next loop due to bounds checks)
            j += 1

        return 0
