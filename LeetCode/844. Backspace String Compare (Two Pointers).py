class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        first = len(s)
        second = len(t)

        max_len = max(first, second)
        first_bac = 0
        sec_bac = 0
        let1 = ''
        end = False
        for i in range(max_len):

            while True:
                first -= 1

                if first == -1:
                    end = True
                    break

                let1 = s[first]
                if let1 == '#':
                    first_bac += 1
                else:
                    if first_bac > 0:
                        first_bac -= 1
                    else:
                        break

            while True:
                second -= 1

                if second == -1:
                    end = True
                    break

                let2 = t[second]
                if let2 == '#':
                    sec_bac += 1
                else:
                    if sec_bac > 0:
                        sec_bac -= 1
                    else:
                        break

            if end:
                break

            print(let1)
            print(let2)
            if let1 != let2:
                return False

        return first == second


if __name__ == '__main__':
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))
    print(sol.backspaceCompare("ab##", "c#d#"))
    print(sol.backspaceCompare("a#c", "b"))
