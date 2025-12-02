class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = set()

        def backtrack(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                res.add(word)
            
            backtrack(r+1, c, node, word)
            backtrack(r-1, c, node, word)
            backtrack(r, c+1, node, word)
            backtrack(r, c-1, node, word)
            visited.remove((r,c))
        

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c, root, "")
        return list(res)

        