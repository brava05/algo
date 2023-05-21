class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        if right == 0:
            return nums[right]

        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(sol.findMin([11,13,15,17]))
