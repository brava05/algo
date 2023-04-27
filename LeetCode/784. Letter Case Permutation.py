class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
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
    print(sol.letterCasePermutation("a1b22"))