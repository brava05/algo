class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def helper(cur_target, path, ind):
            if cur_target < 0:
                return
            elif cur_target == 0:
                res.append(path)
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                helper(cur_target - candidates[i], path + [candidates[i]], i + 1)

        candidates.sort()
        res = []
        helper(target, [], 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
