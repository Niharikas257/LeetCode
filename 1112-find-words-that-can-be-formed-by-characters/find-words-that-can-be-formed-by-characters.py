class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)
            for char in word_count:
                if word_count[char]>chars_count.get(char,0):
                    break

            else:
                total_length += len(word)

        return total_length
    
        