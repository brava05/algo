class Solution:
    def rob(self, nums: list[int]) -> int:

        def helper_rob(loc_nums):
            rob = 0
            not_rob = 0

            for val in loc_nums:
                rob, not_rob = not_rob + val, max(rob, not_rob)

            return max(rob, not_rob)

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(helper_rob(nums[:len(nums) - 1]), helper_rob(nums[1:]))

if __name__ == '__main__':
    sol = Solution()
    # print(sol.rob([2, 1]))
    # print(sol.rob([1, 2]))
    # print(sol.rob([2, 3, 2]))
    # print(sol.rob([1, 2, 3, 2]))
    # print(sol.rob([5, 2, 3, 1]))
    print(sol.rob([1, 2, 1, 1]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([1, 3, 1, 3, 100]))

