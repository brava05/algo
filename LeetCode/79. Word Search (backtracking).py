from collections import defaultdict
from collections import Counter
class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:
        def bfs(row, col, ind, used):
            if ind == len(word) - 1:
                return True

            orient = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for r, c in orient:
                new_row = row + r
                new_col = col + c
                if new_col == -1 or new_col == len(board[0]):
                    continue
                if new_row == -1 or new_row == len(board):
                    continue
                if (new_row, new_col) in used:
                    continue

                if board[new_row][new_col] == word[ind + 1]:
                    used.append((new_row, new_col))
                    res = bfs(new_row, new_col, ind + 1, used)
                    if res: return res
                    used.remove((new_row, new_col))

            return False

        if len(board) == 0: return False
        if len(word) == 0: return False

        # сверяем количество букв и их наличие в слове перед запуском backtraking
        boardDic = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardDic[board[i][j]] += 1

        wordDic = Counter(word)
        for c in wordDic:
            if c not in boardDic or boardDic[c] < wordDic[c]:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used = [(i, j)]
                    res = bfs(i, j, 0, used)
                    if res: return res
        return False


if __name__ == '__main__':
    sol = Solution()
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # print(sol.exist(board, "ABCCED"))
    # board = [["A", "B", "C", "E"]]
    # print(sol.exist(board, "ABC"))
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # print(sol.exist(board, "ABBCCED"))
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # print(sol.exist(board, "SEE"))
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # print(sol.exist(board, "ABCB"))
    # board = [["a", "a"]]
    # print(sol.exist(board, "aaa"))
    # board = [["a", "b"], ["c", "d"]]
    # print(sol.exist(board, "acdb"))
    # board = [["A", "B", "C", "E"],
    #          ["S", "F", "E", "S"],
    #          ["A", "D", "E", "E"]]
    # print(sol.exist(board, "ABCEFSADEESE"))
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
     ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
    print(sol.exist(board, "AAAAAAAAAAAAAAa"))