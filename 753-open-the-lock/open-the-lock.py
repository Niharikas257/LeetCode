class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        start = "0000"
        q = deque([(start, 0)]) # state, moves
        if start in dead:
            return -1
        if target == start:
            return 0
        if target in dead:
            return -1
        visited = set([start])

        while q:
            state, moves = q.popleft()
            for neighbor in self.neighbors(state):
                if neighbor in dead or neighbor in visited:
                    continue
                if neighbor == target:
                    return moves+1
                visited.add(neighbor)
                q.append((neighbor, moves+1))
        return -1
                
        
    
    def neighbors(self, state):
        res  = []
        s = list(state)
        for i in range(4):
            original = s[i]
            digit = ord(original) - ord('0')
            s[i] = chr(((digit+1)%10) + ord('0'))
            res.append("".join(s))
            s[i] = chr(((digit-1)%10) + ord('0'))
            res.append("".join(s))
            s[i] = original
        return res


