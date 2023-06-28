class Solution:
    max_pol = ''

    def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0] * len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True


        longest_palindrom = ''

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        if len(longest_palindrom) < len(s[i:j + 1]):
                            longest_palindrom = s[i:j + 1]

        return longest_palindrom

    def longestPalindrome_my(self, s: str) -> str:
        self.max_pol = ''
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if len(self.max_pol) < (r - l -1):
                self.max_pol = s[l + 1:r]

        for i in range(len(s)):
            helper(i, i + 1)
            helper(i, i)

        return self.max_pol


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('baabad'))
    print(sol.longestPalindrome('aaasssaad'))
