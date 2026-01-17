# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         rows = len(board)
#         cols = len(board[0])
#         visited = [[False]*cols for _ in range(rows)]
#         directions = [(0,1), (0,-1), (1,0), (-1,0)]

#         def dfs(row, col):
#             if row<0 or col<0 or row>= rows or col >= cols:
#                 return
            
#             if board[row][col] != 'O':
#                 return

#             board[row][col] = 'T'
#             dfs(row+1, col)
#             dfs(row-1, col)
#             dfs(row, col+1)
#             dfs(row, col-1)
#         # You can start from anywhere but it is optimized to start from the edges and going inside (This is even more relevant in this case because the 0's at the edges are not supposed to change).
           
#         for r in range(rows):
#             if board[r][0] == "O":
#                 dfs(r, 0)
#             if board[r][cols - 1] == "O":
#                 dfs(r, cols - 1)

#         for c in range(cols):
#             if board[0][c] == "O":
#                 dfs(0, c)
#             if board[rows - 1][c] == "O":
#                 dfs(rows - 1, c)

#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "O":
#                     board[r][c] = "X"
#                 elif board[r][c] == "T":
#                     board[r][c] = "O"


#         # Start from the edges where the cell is zero because that could be a leak point. 
#         # If there is no zero at the edge, then you simly traverse all the rows and cols and flip them
#         # You should preserve the zeros at the edge by converting it to T and then at the end flip it back to zero


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        regions = []
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def isValid(row, col):
            # If cell lies out of bounds
            if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0])):
                return False
            # Otherwise
            return True

        def dfs(x,y, sol):
            sol.append((x,y))
            visited[x][y] = True
            # board[x][y] = 'X'
            
            q = deque()
            q.append((x,y))

            while q:
                # print(q)
                row, col = q.pop()
                for i in range(len(dx)):
                    tempRow = row + dx[i]
                    tempCol = col + dy[i]
                    if isValid(tempRow, tempCol) and board[tempRow][tempCol] == 'O' and not visited[tempRow][tempCol]:
                        # board[tempRow][tempCol] = 'X'
                        visited[tempRow][tempCol] = True
                        sol.append((tempRow, tempCol))
                        q.append((tempRow, tempCol))
            for i,j in sol:
                if i == 0 or j == 0 or i == (len(board)-1) or j == (len(board[0]) - 1):
                    return
            
            for i,j in sol:
                board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and not visited[i][j]:
                    dfs(i,j, [])
                    # regions +=1
        return regions
