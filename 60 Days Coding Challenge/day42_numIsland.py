def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count +=1
                dfs(r, c)
    return count
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

grid = []
for i in range(rows):
    row = input(f"Enter row {i+1}: ").split()
    grid.append(row)

print(grid)
print(numIslands(grid))