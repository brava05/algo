from sys import maxsize


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0
        res = 1000000
        cur = nums[right]
        while left < len(nums):

            if cur >= target:
                res = min(res, right - left + 1)
                left += 1
                cur -= nums[left - 1]
                if left >= right:
                    right = left
            else:
                if right == len(nums) - 1:
                    break
                right += 1
                cur += nums[right]
        return 0 if res == 1000000 else res

    def minSubArrayLen_leet(self, s, nums):
        res = maxsize
        left, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1

        return res if res != maxsize else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen_leet(7, [2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen(4, [1, 1, 4]))
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(sol.minSubArrayLen(8, [1, 1, 1, 1, 1, 1, 1, 1]))
