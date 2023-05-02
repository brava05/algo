class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        # из строки получаются все варианты если буквы использовать в upper ahn lower
        res = []
        stack = [(s, "")]
        while stack:
            line, new_path = stack.pop()
            if line == "":
                res.append(new_path)
            for i in range(len(line)):
                new_line = line[i+1:]
                letter = line[i]
                # new_path = new_path + letter

                if letter.isalpha():
                    if letter.islower():
                        stack.append((new_line, new_path + letter))
                        stack.append((new_line, new_path + letter.upper()))
                    else:
                        stack.append((new_line, new_path + letter))
                        stack.append((new_line, new_path + letter.lower()))
                    break
                else:
                    # это не буква добавляем в ответ если это последний символ в строке
                    new_path += letter
                    if i == len(line)-1:
                        res.append(new_path)
        return res

    def letterCasePermutation_LeetCode1(self, s: str) -> list[str]:
        def backtrack(start, subset):
            if len(subset) == len(s):
                res.append(subset[:])
                return

            for i in range(start, len(s)):
                if s[i].isdigit():
                    backtrack(i + 1, subset + s[i])
                else:
                    lower_subset = subset + s[i].lower()
                    backtrack(i + 1, lower_subset)
                    upper_subset = subset + s[i].upper()
                    backtrack(i + 1, upper_subset)

        res = []
        backtrack(0, "")
        return res

    def letterCasePermutation_LeetCode2(self, s: str) -> list[str]:
        res = []
        n = len(s)
        seen = set()  # Set to keep track of unique strings
        for i in range(2 ** n):
            temp = ""
            for j in range(n):
                if (i >> j) & 1:
                    temp += s[j].upper()
                else:
                    temp += s[j].lower()
            if temp not in seen:  # Add string to output only if it hasn't been added before
                res.append(temp)
                seen.add(temp)
        return res


def letterCasePermutationWhithLetterPerm(self, s: str) -> list[str]:
    # эта процедура еще и переставляет все символы
    res = []
    stack = []
    stack.append((s, ""))
    while stack:
        line, path = stack.pop()
        if line == "":
            res.append(path)
        for i in range(len(line)):
            new_line = line[:i] + line[i + 1:]
            letter = line[i]
            new_path = path + letter
            stack.append((new_line, new_path))
            if letter.isalpha():
                if letter.islower():
                    new_path = path + letter.upper()
                    stack.append((new_line, new_path))
                else:
                    new_path = path + letter.lower()
                    stack.append((new_line, new_path))

    return res




if __name__ == '__main__':
    sol = Solution()
    # print(sol.letterCasePermutation("a1b22"))
    # print(sol.letterCasePermutation_LeetCode1("a1b22"))
    print(sol.letterCasePermutation_LeetCode2("a1b22"))
