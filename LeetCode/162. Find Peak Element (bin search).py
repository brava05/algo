class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        nums_len = len(nums)
        if nums_len == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[nums_len - 1] > nums[nums_len - 2]:
            return nums_len - 1

        left = 1
        right = nums_len - 2

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        left = 0
        right = nums_len - 1

        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > nums[mid - 1]:
                left = mid
            else:
                right = mid - 1
        return left

        return -1

    def findPeakElement_leet(self, nums):
        beg, end = 0, len(nums) - 1
        while beg < end:
            mid = (beg + end) // 2
            if nums[mid] < nums[mid + 1]:
                beg = mid + 1
            else:
                end = mid

        return end


if __name__ == '__main__':
    sol = Solution()
    # print(sol.findPeakElement([1, 2, 1, 2, 5, 6, 6]))
    print(sol.findPeakElement([1, 2, 1, 2, 5, 6, 6]))
