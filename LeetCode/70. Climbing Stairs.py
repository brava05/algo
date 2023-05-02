class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n + 1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs_LeetCode(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one + two
            one = two
            two = temp
        return two

if __name__ == '__main__':
    sol = Solution()

    print(sol.climbStairs(4))