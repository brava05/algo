class Solution:
    def search(self, nums, target):
        # находим первое число которое меньше или равно искомому
        # поэтому вместо if nums[mid] <= target: у нас if nums[mid] < target:
        left = 0
        len_n = len(nums)
        right = len_n - 1
        while left < right:
            cur = (right + left) // 2
            if nums[cur] < target:
                left = cur + 1
            else:
                right = cur
        return left

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        len_n = len(nums)
        if len_n == 0:
            return [-1, -1]

        first = self.search(nums, target)
        last = self.search(nums, target + 1) - 1

        if first <= last:
            return [first, last]
        else:
            # из-за условия -1 у нас вернется last меньше чем first если число не нашли
            return [-1, -1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 8, 10], 8))
    print(sol.searchRange([2, 5, 7, 7, 8, 8, 8, 10], 5))
    print(sol.searchRange([5, 7, 8, 8, 8, 10], 6))
