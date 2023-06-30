class Solution:
    def wordBreak(self, s, words):
        ok = [True]
        max_len = max(map(len, words + ['']))
        words = set(words)
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in words for j in range(max(0, i - max_len), i)),
        return ok[-1]

    def wordBreak2(self, s, words):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for w in words:
                if dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
        return dp[-1]

    def wordBreak_rekurs(self, s: str, wordDict: list[str]) -> bool:
        longest = 0

        def helper(newstr):
            if newstr == '':
                return True
            cur = ''
            for i in range(longest):
                if i == len(newstr):
                    return False
                cur += newstr[i]
                if cur in wordDict:
                    if helper(newstr[i + 1:]):
                        return True

            return False

        set_w = set()
        for word in wordDict:
            set_w = set_w.union(set(word))
            if len(word) > longest:
                longest = len(word)

        set_s = set(s)
        if len(set_s - set_w) > 0:
            return False

        return helper(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak("applepenapple", ["apple", "pen"]))
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
    print(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
