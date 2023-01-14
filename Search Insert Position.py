# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0:
            if nums[left-1] < target:
                return left
            else:
                return left-1
        else:
            return 0





if __name__ == "__main__":
    nums = [2, 5, 6, 9]
    target = 5
    sol = Solution()
    print(sol.searchInsert(nums, target))

