from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_words_length = word_length * num_words
        word_count = Counter(words)  # Count frequency of each word
        result = []

        # Loop over the starting points within word length
        for start in range(word_length):
            left = start  # Left boundary of the sliding window
            seen_words = {}
            count = 0  # Number of valid words in the current window

            # Slide the window over the string in word_length chunks
            for right in range(start, len(s) - word_length + 1, word_length):
                word = s[right:right + word_length]

                # If word is in the list of words, process it
                if word in word_count:
                    seen_words[word] = seen_words.get(word, 0) + 1
                    count += 1

                    # If the word is seen too many times, move the left boundary
                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        left += word_length

                    # If the current window has exactly the same number of words, record the result
                    if count == num_words:
                        result.append(left)

                # If the word is not in the list, reset the window
                else:
                    seen_words.clear()
                    count = 0
                    left = right + word_length

        return result

# # Example usage:
# s = "barfoothefoobarman"
# words = ["foo", "bar"]
# solution = Solution()
# print(solution.findSubstring(s, words))  # Output: [0, 9]
