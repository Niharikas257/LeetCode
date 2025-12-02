class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.end = True
        return cur.end

    def search(self, word: str) -> bool:
        def backtrack(j, root):
            node = root
            if j == len(word):
                return node.end
            
            for ch in range(j, len(word)):
                if word[ch] == '.':
                    for child in node.children.values():
                        # path.append(node[child])
                        if backtrack(ch+1, child):
                            return True
                    return False
                else:
                    if word[ch] not in node.children:
                        return False
                    node = node.children[word[ch]]
            return node.end
        return backtrack(0,self.root)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)