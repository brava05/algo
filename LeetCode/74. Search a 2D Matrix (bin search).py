class Solution:
    def find_row(self, matrix, target):
        left = 0
        right = len(matrix)

        if right == 0:
            return 0

        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target:
                left = mid + 1
            else:
                right = mid

        return left - 1
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        row = self.find_row(matrix, target)
        left = 0
        right = len(matrix[row])
        while left < right:
            mid = (left + right) // 2
            if matrix[row][mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0 and matrix[row][left-1] == target:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11))
    print(sol.searchMatrix([[1]], 3))
    print(sol.searchMatrix([[1], [3]], 3))
