class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # здесь собираются подмассивы.
        # не любые значения из массива, произвведение которых меньше К а именно по порядку
        # количество подмассивов между левым и правым краем считается как прав-лев+1
        count = 0
        left = 0
        right = 0
        prod = 1
        for right in range(len(nums)):
            prod = prod * nums[right]

            while prod >= k and left <= right:
                prod = prod / nums[left]
                left += 1

            count += right - left +1

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(sol.numSubarrayProductLessThanK([1, 2, 3], 0))
