class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
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


if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))
    print(sol.findAnagrams("abab", "ab"))
