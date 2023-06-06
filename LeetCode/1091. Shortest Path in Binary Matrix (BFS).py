from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        deq = deque()
        deq.append((0,0))
        while deq:
            i, j = deq.popleft()




if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
    # print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
