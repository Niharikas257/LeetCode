class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        n = len(s)
        total_shift = 0  # Maintain cumulative shift
        result = list(s)  # Convert string to list (strings are immutable)

        # Iterate in reverse to accumulate shifts
        for i in range(n - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26  # Accumulate shift with modulo
            new_char = chr(((ord(result[i]) - ord('a') + total_shift) % 26) + ord('a'))  
            result[i] = new_char  # Update the character in list

        return "".join(result)  # Convert list back to string