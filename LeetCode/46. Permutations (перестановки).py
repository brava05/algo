class Solution:
    # https://www.youtube.com/watch?v=oK8A7eIWXF8
    def left_shift(self, comb, k):
        # k = len(comb)
        first = comb[0]
        for i in range(k):
            comb[i] = comb[i + 1]
        comb[k] = first

    def indexes_to_list(self, comb_index, list_mat):
        res = []
        for ind in comb_index:
            res.append(list_mat[ind])
        return res

    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        k = len(nums) - 1
        n = k
        comb = [i for i in range(k + 1)]
        # res.append(comb.copy())
        res.append(self.indexes_to_list(comb, nums))
        while k > 0:
            self.left_shift(comb, k)
            if comb[k] != k:
                # res.append(comb.copy())
                res.append(self.indexes_to_list(comb, nums))
                k = n
            else:
                k -= 1

        return res

    def perm_DFS_leetcode(self, nums):
        stack = [(nums, [])]  # -- nums, path (or perms)
        res = []
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):  # -- NOTE [4]
                newNums = nums[:i] + nums[i + 1:]
                stack.append((newNums, path + [nums[i]]))
        return res

    def perm_BFS_leetcode(self, nums):
        from collections import deque
        q = deque()
        q.append((nums, []))  # -- nums, path (or perms)
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i + 1:]
                q.append((newNums, path + [nums[i]]))
        return res


if __name__ == '__main__':
    sol = Solution()

    print(sol.permute([1, 2, 3]))
    # print(sol.permute([0, 1, 2]))
    print(sol.perm_DFS_leetcode([1, 2, 3]))
    print(sol.perm_BFS_leetcode([1, 2, 3]))
