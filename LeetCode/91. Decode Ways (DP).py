class Solution:
    def numDecodings(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0 or s[0] == "0":
            return 0

        if len_s == 1:
            return 1

        prev = 1
        pprev = 1
        cur = 0
        for i in range(1, len_s):
            if int(s[i]) > 0:
                cur = prev
            else:
                cur = 0
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                cur = cur + pprev

            pprev = prev
            prev = cur

        return cur

    def numDecodings_leet(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]):  # (2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings("226"))
    print(sol.numDecodings_leet("226"))
    print(sol.numDecodings("1"))
    print(sol.numDecodings_leet("1"))
    print(sol.numDecodings("10"))
    print(sol.numDecodings_leet("10"))
    print(sol.numDecodings("2101"))
    print(sol.numDecodings_leet("2101"))
