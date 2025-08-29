class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not s or not words:
            return []
        
        each_word_len = len(words[0])
        total_words_len = len(words)
        total_len = each_word_len * total_words_len
        Target_count = Counter(words) # This will count and save the frequency of all the words in the array and the frequency that we are targeting.

        for i in range(each_word_len):
            left = i
            count = 0
            window_count = Counter()

            for j in range(i, len(s)-each_word_len +1, each_word_len):
                word = s[j:j+each_word_len]

                if word in Target_count: # now there are 2 cases, either we have found the word or we have found the word but the frequency in our window exceeds the target count we needed.
                    window_count[word] += 1
                    count += 1

                    while window_count[word]>Target_count[word]:
                        left_word  = s[left:left+each_word_len]
                        window_count[left_word] -=1
                        count-=1
                        left += each_word_len
                    
                    if count == total_words_len:
                        res.append(left)

                else:
                    window_count.clear()
                    count = 0
                    left = j + each_word_len
            
        return res


        