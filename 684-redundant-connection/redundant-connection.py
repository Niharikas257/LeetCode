# class UF:
#     def __init__(self,n):
#         self.parent = [i for i in range(n+1)]
#         self.rank = [0]*(n+1)
#         self.count = n

#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, a, b):
#         root_a = self.find(a)
#         root_b = self.find(b)

#         if root_a == root_b:
#             return False
            
#         if self.rank[root_a] < self.rank[root_b]:
#             self.parent[root_a] = root_b
#         elif self.rank[root_b] < self.rank[root_a]:
#             self.parent[root_b] = root_a
#         else:
#             self.parent[root_b] = root_a
#             self.rank[root_a] += 1
#         return True

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         n = len(edges)
#         uf = UF(n)
#         for (u,v) in edges:
#             if not uf.union(u,v):
#                 return [u,v]

#         return []

class Union_Find:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.count = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_b] < self.rank[root_a]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
        
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        UF = Union_Find(len(edges))
        for u,v in edges:
            if not UF.union(u,v):
                return [u,v]
        return []


            
            
            