class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(loc_nums, loc_path, loc_res):
            loc_res.append(loc_path)
            for i in range(len(loc_nums)):
                dfs(loc_nums[i+1:], loc_path+[loc_nums[i]], loc_res)

        res = []
        path = []
        dfs(nums, path, res)
        return res
    def subsets2(self, nums: list[int]) -> list[list[int]]:
        # медленнее и больше памяти забирает
        res = [[]]
        for i in sorted(nums):
            res += [item+[i] for item in res]
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    print(sol.subsets2([1, 2, 3]))
