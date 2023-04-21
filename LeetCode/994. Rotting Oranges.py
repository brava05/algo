# 0 - нет апельсина
# 1 - свежий апельсин
# 2 - гнилой
# за 1 шаг один апельсин рядом с гнилым становится тоже гнилым
# вопрос - когда все сгниют
from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:

        good_oranges = []
        bad_deq = deque()
        next_deq = deque()
        DIR_col = [0, 1, 0, -1]
        DIR_row = [1, 0, -1, 0]
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            line = grid[i]
            for j in range(m):
                if line[j] == 1:
                    good_oranges.append((i, j))
                elif line[j] == 2:
                    bad_deq.append((i, j))

        if not good_oranges:
            return 0

        step = 1
        while step < m+n+1:

            if bad_deq:
                i, j = bad_deq.popleft()
                for c in range(4):
                    ni = i + DIR_row[c]
                    nj = j + DIR_col[c]

                    if ni < 0 or ni == n or nj < 0 or nj == m:
                        continue
                    if grid[ni][nj] != 1:
                        continue
                    next_deq.append((ni, nj))
                    good_oranges.remove((ni, nj))
                    grid[ni][nj] = 2
                    if not good_oranges:
                        return step
            else:
                step += 1
                if next_deq:
                    bad_deq = next_deq
                    next_deq = deque()
                else:
                    return -1

        return -1


if __name__ == "__main__":
    sol = Solution()
    # matrix = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # matrix = [[2,1,1],[0,1,1],[1,0,1]]
    matrix = [[0,2]]
    print(sol.orangesRotting(matrix))
