class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def backtrack(res, cur, ind):
            # print(cur)
            # for i in range(ind, len(digits)):
            for letter in let_dict[digits[ind]]:
                if ind == len(digits)-1:
                    res.append(cur+letter)
                else:
                    backtrack(res, cur+letter, ind+1)

        let_dict = {"1": [""],
                    "2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"]}
        res = []
        if digits == "":
            return res
        backtrack(res, "", 0)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations("23"))
    print(sol.letterCombinations("12"))
    print(sol.letterCombinations(""))
