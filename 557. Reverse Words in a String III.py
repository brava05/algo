class Solution:
    def reverseWords(self, s: str) -> str:
        worfList = s.split(" ")
        res = ""
        for word in worfList:
            res = res + word[::-1]+" "
        return res[0:len(res)-1]


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    sol = Solution()
    
    s = sol.reverseWords(s)
    print(s)
    # Input: s = "Let's take LeetCode contest"
    # Output: "s'teL ekat edoCteeL tsetnoc"