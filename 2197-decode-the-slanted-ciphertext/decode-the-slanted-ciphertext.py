class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # if not encodedText:
        #     return ""  # Edge case: Empty input
        if len(encodedText) == '0':
            return " "
        
        cols = len(encodedText) // rows + 1
        matrix = [encodedText[i * cols:(i + 1) * cols] for i in range(rows)] 

        originalText = []
        
        # Traverse diagonally
        for col in range(cols):
            for row in range(rows):
                # if col + row < cols:  # Ensure within bounds
                if col < len(matrix[row]):
                    originalText.append(matrix[row][col])
        
        return "".join(originalText).rstrip()
        
