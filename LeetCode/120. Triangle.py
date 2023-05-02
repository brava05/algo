class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]
        prev = [triangle[0][0]]

        for i in range(1, n):
            cur = []
            line = triangle[i]
            for j in range(len(line)):
                if j == 0:
                    cur.append(prev[j] + line[j])
                elif j == len(prev):
                    cur.append(prev[j - 1] + line[j])
                else:
                    cur.append(min(prev[j], prev[j - 1]) + line[j])
            prev = cur

        return min(prev)

    def minimumTotal_leetCode(self, t: list[list[int]]) -> int:
        for i in range(len(t) - 2, -1, -1):
            for j in range(i + 1):
                t[i][j] += min(t[i + 1][j], t[i + 1][j + 1])

        return t[0][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(sol.minimumTotal_leetCode([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
