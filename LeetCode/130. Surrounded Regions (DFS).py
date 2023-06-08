class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # я от нуля шел до края - и если по DFS доходил до края, значит оставляем нули.
        # на лит коде есть другое - более оптимальное движение - он края, все нули добавляем в дек
        # и дальше от каждого нуля ищем еще соседние нули через BFS - d след раз можно так реализовать
        m = len(board)
        n = len(board[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(stack, visited):
            while stack:
                i, j = stack.pop()
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    return True
                for x, y in dir:
                    if board[i + x][j + y] == "O" and (i + x, j + y) not in visited:
                        visited.add((i + x, j + y))
                        stack.append((i + x, j + y))
            return False

        for line in range(len(board)):
            for col in range(len(board[0])):
                if board[line][col] == "O":
                    stack = [(line, col)]
                    visited = set()
                    visited.add((line, col))
                    cell_is_free = dfs(stack, visited)
                    if not cell_is_free:
                        for i, j in visited:
                            board[i][j] = "X"


if __name__ == '__main__':
    sol = Solution()
    # board = [["X", "X", "X", "X"],
    #          ["X", "O", "O", "X"],
    #          ["X", "X", "O", "X"],
    #          ["X", "O", "X", "X"]]
    # sol.solve(board)
    # print(board)

    # board = [["O", "O", "O"],
    #          ["O", "O", "O"],
    #          ["O", "O", "O"],
    #          ["O", "O", "O"]]
    board = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
             ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
             ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
             ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
             ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
             ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
             ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
             ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
             ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]
    sol.solve(board)
    print(board)
