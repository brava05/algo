class Solution:
    def findAnagrams_naiv(self, s: str, p: str) -> list[int]:
        list_p = list(p)
        list_p.sort()
        len_p = len(p)
        list_s = list(s)
        res = []
        for i in range(len(list_s) - len_p + 1):
            print(i)
            new = list_s[i: i + len_p]
            new.sort()
            if new == list_p:
                res.append(i)
        return res

    def findAnagrams(self, s: str, p: str) -> list[int]:
        dict_letter = {}
        res = []
        len_p = len(p)
        for letter in p:
            dict_letter[letter] = dict_letter.get(letter, 0) - 1

        for i in range(len(s)):
            dict_letter[s[i]] = dict_letter.get(s[i], 0) + 1
            if i >= len_p:
                dict_letter[s[i - len_p]] = dict_letter.get(s[i - len_p], 0) - 1
            if all(v == 0 for v in dict_letter.values()):
                res.append(i - len_p + 1)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))
    print(sol.findAnagrams("abab", "ab"))
