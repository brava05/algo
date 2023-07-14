from bisect import bisect_left


class Solution:

    # https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
    # там еще есть решения с деревьями, на которые я пока не отважился смотреть даже
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)

    def lengthOfLIS_DP(self, nums: list[int]) -> int:
        # Time: O(N^2)
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLIS_no_good(self, nums: list[int]) -> int:
        l = 0
        r = 1
        res = 0
        while r < len(nums):
            if nums[r] > nums[r - 1]:
                res = max(res, r - l + 1)
            else:
                l = r
            r += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
