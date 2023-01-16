class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)
    # Input: nums = [0,1,0,3,12]
    # Output: [1,3,12,0,0]