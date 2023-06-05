class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(y, x):
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
                return
            if grid[y][x] != '1':
                return
            grid[y][x] = '2'

            dfs(y + 1, x)
            dfs(y, x + 1)
            dfs(y - 1, x)
            dfs(y, x - 1)

        if not grid:
            return 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1

        return cnt


if __name__ == '__main__':
    sol = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(sol.numIslands(grid))
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(sol.numIslands(grid))
