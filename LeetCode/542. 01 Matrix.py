from collections import deque


class Solution:

    def updateMatrix(self, mat):
        # BFS approach
        DIR_lines   = [0, 1, 0, - 1]
        DIR_columns = [1, 0, -1, 0]
        n = len(mat)
        m = len(mat[0])
        deq = deque()
        for i in range(n):
            line = mat[i]
            new_line = [0]*m
            for j, cell in enumerate(line):
                if cell == 0:
                    deq.append((i,j))
                else:
                    line[j] = -1
        while deq:
            i, j = deq.popleft()
            for c in range(4):
                ni = i + DIR_lines[c]
                nj = j + DIR_columns[c]
                if ni == n or ni < 0 or nj == m or nj < 0:
                    continue
                if mat[ni][nj] != -1:
                    continue
                mat[ni][nj] = mat[i][j] + 1
                deq.append((ni, nj))

        return mat



    def updateMatrix2(self, mat):
        # DP approach
        res = []
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            line = mat[i]
            new_line = [0]*m
            for j, cell in enumerate(line):
                if cell != 0:
                    if j == 0:
                        left = 10000
                    else:
                        left = new_line[j-1]
                    if i == 0:
                        top = 10000
                    else:
                        top = res[i-1][j]
                    new_line[j] = (min(left+1, top+1))

            res.append(new_line)

        # back side
        for i in range(n-1, -1, -1):
            line = mat[i]
            new_line = res[i]
            for j in range(m-1, -1, -1):
                cell = line[j]
                if cell != 0:
                    if j == m-1:
                        right = 10000
                    else:
                        right = new_line[j+1]
                    if i == n-1:
                        down = 10000
                    else:
                        down = res[i+1][j+1]
                    new_line[j] = (min(right+1, down+1, new_line[j]))

        return res


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 0, 0],[1, 1, 0], [1, 1, 1]]
    print(sol.updateMatrix(matrix))
