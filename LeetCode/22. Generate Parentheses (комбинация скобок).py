class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(cur, open, close):
            if open == n and close == n:
                res.append(cur)
                return
            if open <= n:
                backtrack(cur + "(", open + 1, close)
            if open > close and close < n:
                backtrack(cur + ")", open, close + 1)

        res = []
        backtrack("", 0, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(0))
