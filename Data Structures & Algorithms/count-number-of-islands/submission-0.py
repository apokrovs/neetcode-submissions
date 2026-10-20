class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        def explore(r:int, c:int):
            if r > rows-1 or r< 0 or c< 0 or c > cols-1 or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            positions = [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            for pos in positions:
                explore(pos[0],pos[1])
        
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    print(r,c)
                    count+=1
                    explore(r,c)
        return count