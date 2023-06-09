class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        graph_l = len(graph)
        stack = [(0, [0])]
        res = []
        while stack:
            node, root = stack.pop()
            if node == graph_l-1:
                res.append(root)
            for i in graph[node]:
                new_root = root.copy()
                new_root.append(i)
                stack.append((i, new_root))

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
    # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
