class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        def dfs(loc_nums, loc_path, loc_res):
            loc_res.append(loc_path)
            for i in range(len(loc_nums)):
                if i > 0 and loc_nums[i] == loc_nums[i - 1]:
                    continue
                dfs(loc_nums[i + 1:], loc_path + [loc_nums[i]], loc_res)

        res = []
        path = []
        nums.sort()
        dfs(nums, path, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 2]))
