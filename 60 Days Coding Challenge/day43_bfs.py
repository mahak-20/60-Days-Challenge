from collections import deque
def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1),
         (0,1), (1, -1), (1, 0), (1, 1)
    ]

    queue = deque([(0,0,1)])
    grid[0][0] = 1
    while queue:
        row, col, length = queue.popleft()
        if row == n-1 and col == n-1:
            return length
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            if (0 <= nr < n and 0<=nc<n and grid[nr][nc] == 0):
                queue.append((nr, nc, length+1))
                grid[nr][nc] = 1

    return -1

n= int(input("Enter the size of grid: "))
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(shortestPathBinaryMatrix(grid))