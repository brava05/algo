class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        temp = []
        self.backtrack(res, temp, nums)
        return res

    def backtrack(self, res, temp, nums):
        if len(nums) == 0:
            res.append(temp)
        for i in range(len(nums)):
            if i + 1 == len(nums) or nums[i] != nums[i+1]:
                self.backtrack(res, temp + [nums[i]], nums[:i] + nums[i + 1:])

    def permuteUnique3(self, nums):
        # очень умно решили с убиранием дублей - я не понимаю пока почему так пропускаются
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: break  # handles duplication
            ans = new_ans
        return ans

    def permuteUnique2(self, nums):
        ans = [[]]
        for n in nums:
            ans = [l[:i] + [n] + l[i:]
                   for l in ans
                   for i in range((l + [n]).index(n) + 1)]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1, 2, 1]))
    print(sol.permuteUnique([1, 2, 3]))
