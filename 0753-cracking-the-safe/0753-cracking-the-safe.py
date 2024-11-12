class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        visited = set()
        s = "0" * (n-1)
        result = s
        while True:
            for x in range(k-1, -1, -1):
                if (s,x) not in visited:
                    result += str(x)
                    visited.add((s,x))
                    s = (s + str(x))[1:]
                    break
                    
            else:
                return result
#         result = ["0"] * n  # Initialize as a list of characters
#         visited = set()
#         # visited.add("".join(result))

#         total_combinations = k ** n  # Total number of unique n-digit combinations

#         def dfs(node):
#             if len(visited) == total_combinations:
#                 return True
#             for x in map(str, range(k)):
#                 neighbor = node + x
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     result.append(x)
#                     if dfs(neighbor[1:]):
#                         return True
#                     # Backtracking
#                     visited.remove(neighbor)
#                     result.pop()

#             return False

#         dfs("".join(result[-(n-1):]))
#         return "".join(result)
