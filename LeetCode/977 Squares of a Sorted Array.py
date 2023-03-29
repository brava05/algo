class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        number = len(nums)
        res_array = [None] * number

        left = 0
        right = number - 1

        pointer = number-1

        while left <= right:
            left_sq = nums[left]**2
            right_sq = nums[right]**2

            if left_sq > right_sq:
                res_array[pointer] = left_sq

                left += 1
            else:
                res_array[pointer] = right_sq
                right -= 1

            pointer -= 1

        return res_array
                            



if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    sol = Solution()
    print(sol.sortedSquares(nums))
