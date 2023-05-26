class Solution:
    def backspaceCompare_naiv(self, s: str, t: str) -> bool:

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

    def backspaceCompare(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []
        for i in range(len(s)):
            if s[i] == '#':
                if list_s:
                    list_s.pop()
            else:
                list_s.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if list_t:
                    list_t.pop()
            else:
                list_t.append(t[i])

        return list_s == list_t

if __name__ == '__main__':
    sol = Solution()
    # print(sol.backspaceCompare("ab#c", "ad#c"))
    # print(sol.backspaceCompare("ab##", "c#d#"))
    # print(sol.backspaceCompare("a#c", "b"))
    print(sol.backspaceCompare("y#fo##f", "y#f#o##f"))
