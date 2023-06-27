class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # содержим данные о прошлых ячейках в одной строке, потому что позапрошлые строки
        # уже не используются
        dp = [[1] * n for _ in range(2)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1]
        return dp[(m - 1) & 1][-1]

    def uniquePaths_matrix(self, m: int, n: int) -> int:
        dp = [[1] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1:
                    dp[i][j] = dp[i][j - 1]
                elif j == 1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3, 7))
    print(sol.uniquePaths(3, 2))
