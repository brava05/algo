class Solution:
    def binary_serch(self, nums, target, left = 0, right = None):
        if right == None:
            right = len(nums)-1

        if right < left:
            return -1
       
        mid = (right - left)//2+left

        if nums[mid] == target:
            return mid
        elif right == left:
            return -1
        elif nums[mid] < target:
            return self.binary_serch(nums, target, mid+1, right)
        else:
            return self.binary_serch(nums, target, left, mid-1)
    
    def search(self, nums: list[int], target: int) -> int:
        return(self.binary_serch(nums, target))

class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left<right:
            i = (right + left) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                left = i+1
            elif nums[i] > target:
                right = i-1
        
        if nums[left] == target:
            return left
        return -1

class Solution3:
    def search(self, nums: list[int], target: int) -> int:
        # Set the left and right boundaries
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1

if __name__ == "__main__":
    nums = [6]
    target = 6
    sol = Solution3()
    print(sol.search(nums, target))