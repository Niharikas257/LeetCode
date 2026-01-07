# class DSU:
#     def __init__(self):
#         self.parent = {}
#         self.rank = {}
#     def add(self, x):
#         if x not in self.parent:
#             self.parent[x] = x
#             self.rank[x] = 0
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#     def union(self, a, b):
#         root_a = self.find(a)
#         root_b = self.find(b)
#         if root_a == root_b:
#             return 
#         if self.rank[root_a] < self.rank[root_b]:
#             self.parent[root_a] = root_b
#         elif self.rank[root_b] < self.rank[root_a]:
#             self.parent[rot_b] = root_a
#         else:
#             self.parent[root_a]= root_b
#             self.rank[root_a] +=1 
        

# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         dsu = DSU()
#         email_and_name = {}
#         # result = []
#         for account in accounts:
#             name = account[0]
#             emails = account[1:]

#             for email in emails:
#                 dsu.add(email)
#                 email_and_name[email] = name

#             first_email = emails[0]
#             for email in emails:
#                 dsu.union(first_email, email)
#         group = defaultdict(list)
#         for email in email_and_name:
#             root = dsu.find(email)
#             group[root].append(email)
#         result = []
#         for root, email_list in group.items():
#             email_list.sort()
#             name = email_and_name[root]
#             result.append([name] + email_list)

#         return result
from typing import List, Dict
from collections import defaultdict

class DSU:
    def __init__(self):
        self.parent: Dict[str, str] = {}
        self.rank: Dict[str, int] = {}

    def add(self, x: str) -> None:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x: str) -> str:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: str, b: str) -> None:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        # Union by rank
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name: Dict[str, str] = {}

        # 1) Union emails within each account
        for account in accounts:
            name = account[0]
            emails = account[1:]

            if not emails:
                continue

            for email in emails:
                dsu.add(email)
                email_to_name[email] = name

            first_email = emails[0]
            for email in emails[1:]:
                dsu.union(first_email, email)

        # 2) Group emails by DSU root
        groups = defaultdict(list)
        for email in email_to_name:
            root = dsu.find(email)
            groups[root].append(email)

        # 3) Build result
        result = []
        for root, email_list in groups.items():
            email_list.sort()
            name = email_to_name[root]
            result.append([name] + email_list)

        return result


            



        