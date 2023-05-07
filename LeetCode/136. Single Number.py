class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        new_list = []
        for i in nums:
            if i in new_list:
                new_list.remove(i)
            else:
                new_list.append(i)

        return new_list[0]

    def singleNumber_leetCode(self, nums: list[int]) -> int:
        # a ^ 0 = a
        # a ^ a = 0, so every duplicate will become 0
        once = 0
        for i in nums:
            once ^= i
        return once


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([4, 1, 2, 1, 2]))
    print(sol.singleNumber_leetCode([4, 1, 2, 1, 2]))
