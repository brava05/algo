class Solution:
    

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums)-k-1)
        reverse(len(nums)-k, len(nums)-1)
        reverse(0, len(nums)-1)
        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol = Solution()
    print(sol.rotate(nums, k))
    # [5,6,7,1,2,3,4]