class Solution:
    def numberOfArithmeticSlices_my(self, nums: list[int]) -> int:
        res = 0
        len_num = len(nums)
        for i in range(len_num - 2):

            j = i+1
            dif = nums[j] - nums[i]
            while j < len_num - 1:
                j += 1
                if nums[j] - nums[j - 1] == dif:
                    res += 1
                else:
                    break
        return res

    def numberOfArithmeticSlices_dp(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp, dpPrev = 0, 0
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp = dpPrev + 1
            ans += dp
            dpPrev = dp
            dp = 0
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArithmeticSlices([1, 2, 3, 4]))
    # print(sol.numberOfArithmeticSlices([1, 2]))
