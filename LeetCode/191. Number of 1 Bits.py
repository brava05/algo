class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        bin_n = bin_n[2:]
        c = bin_n.count('1')
        return c


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingWeight(1000))
