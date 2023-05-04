class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 2:
            n = n / 2
            if n % 2 != 0:
                return False
        return n == 1 or n == 2

    def isPowerOfTwo_leet_code(self, n):
        return n and not (n & n - 1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(16))
    print(sol.isPowerOfTwo(15))
    print(sol.isPowerOfTwo_leet_code(16))
    print(sol.isPowerOfTwo_leet_code(15))
