class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.land_cnt = 0

        def dfs(cur_x, cur_y):
            for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                nxt_x = cur_x + dx
                nxt_y = cur_y + dy
                if 0 <= nxt_x < len(grid[0]) and 0 <= nxt_y < len(grid):
                    if grid[nxt_y][nxt_x] == "1" and not self.visited[nxt_y][nxt_x]:
                        self.visited[nxt_y][nxt_x] = True
                        dfs(nxt_x, nxt_y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not self.visited[i][j]: 
                    dfs(j, i)
                    self.land_cnt += 1
        
        for v in self.visited:
            print(v)

        return self.land_cnt