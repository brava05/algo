from collections import deque


class Solution:
    def shortestPathBinaryMatrix_complic(self, grid: list[list[int]]) -> int:

        deq = deque()
        len_g = len(grid)

        if grid[0][0] == 1 or grid[len_g - 1][len_g - 1] == 1:
            return -1

        grid[0][0] = 1
        deq.append((0, 0))
        while deq:
            i, j = deq.popleft()
            if i == len_g - 1 and j == len_g - 1:
                return grid[i][j]
            for line in (-1, 0, 1):
                for col in (-1, 0, 1):
                    new_i = i + line
                    new_j = j + col
                    if -1 < new_i < len_g and -1 < new_j < len_g:
                        if grid[new_i][new_j] == 0:
                            deq.append((new_i, new_j))
                            grid[new_i][new_j] = grid[i][j]+1
        return -1

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        deq = deque()
        visited = set()
        len_g = len(grid)

        if grid[0][0] == 1 or grid[len_g - 1][len_g - 1] == 1:
            return -1

        directs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        deq.append((0, 0, 1))
        while deq:
            i, j, dist = deq.popleft()
            if i == len_g - 1 and j == len_g - 1:
                return dist
            for line, col in directs:
                new_i = i + line
                new_j = j + col
                if -1 < new_i < len_g and -1 < new_j < len_g:
                    if grid[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                        deq.append((new_i, new_j, dist + 1))
                        visited.add((new_i, new_j))
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPathBinaryMatrix_complic([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    # print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print(sol.shortestPathBinaryMatrix([[0, 0, 0, 0, 1], [1, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0]]))
