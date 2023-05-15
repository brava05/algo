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

        def findStartingIndex_leet(self, nums, target):
            index = -1  # 5
            low, high = 0, len(nums) - 1  # 6

            while low <= high:  # 7
                mid = low + (high - low) / 2  # 8

                if nums[mid] == target:  # 9
                    index = mid  # 10
                    high = mid - 1  # 11
                elif nums[mid] > target:  # 12
                    high = mid - 1  # 13
                else:  # 14
                    low = mid + 1  # 15

            return index

        def findEndingIndex_leet(self, nums, target):
            index = -1
            low, high = 0, len(nums) - 1

            while low <= high:

                mid = low + (high - low) / 2

                if nums[mid] == target:
                    index = mid
                    low = mid + 1  # 16
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return index


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 8, 10], 8))
    print(sol.searchRange([2, 5, 7, 7, 8, 8, 8, 10], 5))
    print(sol.searchRange([5, 7, 8, 8, 8, 10], 6))
