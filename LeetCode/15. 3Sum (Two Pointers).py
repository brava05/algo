class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for left in range(0, len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            right = len(nums) - 1
            mid = left + 1

            while mid < right:
                cur_sum = nums[left] + nums[mid] + nums[right]
                if cur_sum == 0:
                    res.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
                elif cur_sum < 0:
                    mid += 1
                elif cur_sum > 0:
                    right -= 1

        return res

    def threeSum_naiv(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        cur = [nums[i], nums[j], nums[k]]
                        cur.sort()
                        if cur not in res:
                            res.append([nums[i], nums[j], nums[k]])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([0, 0, 0]))
    print(sol.threeSum([1, -1, -1, 0]))
