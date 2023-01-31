class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]

if __name__ == "__main__":
    s = ["h","e","l","o","1", "2"]
    sol = Solution()
    
    sol.reverseString(s)
    print(s)
    # Input: s = ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]