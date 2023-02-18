class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        colums = len(grid[0])

        visitedGrid = [[0]*colums]*rows
        islendColor = 1
        maxArea = 0

        def countNeibors(r,c):
            # global visitedGrid
            global maxArea

            def areaAvaliable(r,c):
                if grid[r][c] == islendColor and visitedGrid[r][c] == 0:
                    return True
                else:
                    return False

            if grid[r][c] == islendColor:
                maxArea += 1
                visitedGrid[r][c]=1
                if r>=1 and areaAvaliable(r-1,c):
                    countNeibors(r-1, c)
                if r<rows-1  and areaAvaliable(r+1,c):
                    countNeibors(r+1, c)
                if c>=1 and areaAvaliable(r,c-1):
                    countNeibors(r, c-1)
                if c<colums-1 and areaAvaliable(r,c+1):
                    countNeibors(r, c+1)
            else:
                return

        countNeibors(2, 2)
        return maxArea


if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution()
    
    s = sol.maxAreaOfIsland(grid)
    print(s)

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.