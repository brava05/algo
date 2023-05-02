class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        for i in range(3, n):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        return max(dp[n - 1], dp[n - 2])

    def rob_optim(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        minus1 = nums[2] + nums[0]
        minus2 = nums[1]
        minus3 = nums[0]
        for i in range(3, n):
            cur = max(minus2, minus3) + nums[i]
            minus1, minus2, minus3 = cur, minus1, minus2
        return max(minus1, minus2)

    def rob_optim2(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        minus1 = 0
        minus2 = 0
        for i in nums:
            cur = max(minus1, minus2 + i)
            minus1, minus2 = cur, minus1
        return cur


if __name__ == '__main__':
    sol = Solution()

    print(sol.rob_optim2([1,1]))
    print(sol.rob_optim2([1, 2, 3, 1]))
    print(sol.rob_optim2([2,7,9,3,1]))