
class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board)==0: return
        m = len(board)
        n = len(board[0])
        queue = []
        def bfs(x, y):
            if board[x][y] == "O":
                queue.append((x,y))
                fill(x,y)
            while queue:
                curr = queue.pop()
                i,j = curr[0],curr[1]
                fill(i+1,j)
                fill(i-1,j)
                fill(i,j+1)
                fill(i,j-1)
        def fill(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y] != "O":
                return
            queue.append((x,y)) 
            board[x][y] = "D"
        for i in range(m):
            bfs(i,0)
            bfs(i,n-1)

        for j in range(n):
            bfs(0,j)
            bfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
