class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. sort all the respective strings and then compare
        # 2. we use hash table and initialize an array if size 26 for all the strings.
        #     The array will be initialized with zeroes and we increase the value as per the frequency.
        #     Then we will compare the frequency array
        
        # freq = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for ch in s:
        #         count[ord(ch) - ord('a')] += 1
        #     freq[tuple(count)].append(s)
        # return list(freq.values())

        group = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            group[key].append(word)
        return list(group.values())
