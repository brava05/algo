class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        def dfs(i):
            for ind, val in enumerate(isConnected[i]):
                if val and ind not in visited:
                    visited.add(ind)
                    dfs(ind)


        cnt = 0
        visited = set()
        for i in range(len(isConnected)):
            if i in visited:
                continue
            dfs(i)
            cnt += 1

        return cnt


if __name__ == '__main__':
    sol = Solution()
    isConnected = [[2, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(sol.findCircleNum(isConnected))
