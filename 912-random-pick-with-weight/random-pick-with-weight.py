class Solution:

    def __init__(self, w: List[int]):
        self.indices = list(range(len(w)))
        self.prob = [weight/sum(w) for weight in w]

    def pickIndex(self) -> int:
        return random.choices(self.indices, weights = self.prob)[0]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()