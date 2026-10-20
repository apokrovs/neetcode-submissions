from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"

            while queue:
                row, col = queue.popleft()

                neighbors = [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1)
                ]

                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)

        return count