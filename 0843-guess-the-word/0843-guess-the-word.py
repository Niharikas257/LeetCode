# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import random
# class Solution(object):
#     def findSecretWord(self, words, master):
#         """
#         :type words: List[Str]
#         :type master: Master
#         :rtype: None
#         """
#         def count_matches(word1, word2):
#             return sum(c1 == c2 for c1, c2 in zip(word1, word2))
        
#         for _ in range(20):
#             guessed = random.choice(words)
#             matches = master.guess(guessed)
            
#             if matches == 6:
#                 return
#             wordlist = (word for word in words if count_matches(word, guessed) == matches )
            
        
            


class Solution:
    def findSecretWord(self, words, master):
        words = set(words)
        similarity = {}

        # Populate similarity dictionary
        for w1 in words:
            similarity[w1] = {}
            for w2 in words:
                if w1 == w2:
                    continue
                similarity[w1][w2] = sum(c1 == c2 for c1, c2 in zip(w1, w2))

        def pop_most_similar():
            # Find word with maximum similarity to other words
            _, word = max((sum(similarity[w].values()), w) for w in words)
            words.remove(word)
            return word

        for _ in range(10):
            w1 = pop_most_similar()
            score = master.guess(w1)
            if score == 6:
                break
            words = set(w2 for w2 in words if similarity[w1][w2] == score)
