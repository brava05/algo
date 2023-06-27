class Solution:
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
    def jump_my(self, nums: list[int]) -> int:
        len_n = len(nums)
        dp = [10000] * len_n
        dp[0] = 0
        for i in range(0, len_n):
            for j in range(1, nums[i] + 1):
                if i + j >= len_n:
                    continue
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[len_n - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))
    print(sol.jump([2, 3, 0, 1, 4]))
    print(sol.jump([2]))
    print(sol.jump([2, 2, 1, 1, 4]))
    print(sol.jump([2, 6, 1, 1, 6, 1, 1, 1, 1, 1, 1]))
