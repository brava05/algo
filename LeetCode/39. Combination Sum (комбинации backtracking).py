class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        self.helper(candidates, target, [], 0, 0, res)
        return res

    def helper(self, candidates, target, path, cur_sum, ind, res):
        if cur_sum > target:
            return
        elif cur_sum == target:
            res.append(path)
            return

        for i in range(ind, len(candidates)):
            self.helper(candidates, target, path + [candidates[i]], cur_sum + candidates[i], i, res)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def helper(cur_target, path, ind):
            if cur_target < 0:
                return
            elif cur_target == 0:
                res.append(path)
                return

            for i in range(ind, len(candidates)):
                helper(cur_target - candidates[i], path + [candidates[i]], i)

        res = []
        helper(target, [], 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
