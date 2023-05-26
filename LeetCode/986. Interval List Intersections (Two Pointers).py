class Solution:
    def intervalIntersection_leet(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            f_start, f_finish = firstList[i]
            s_start, s_finish = secondList[j]
            if f_start <= s_finish and f_finish >= s_start:
                res.append([max(f_start, s_start), min(f_finish, s_finish)])

            if f_finish <= s_finish:
                i += 1
            else:
                j += 1
        return res

    def intervalIntersection_my(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # операнды поменял местами для правильной сортировки
        # чтобы вначале было добавление, а потом уменьшение
        events = []
        for i in firstList:
            events.append((i[0], -1))
            events.append((i[1], 1))
        for i in secondList:
            events.append((i[0], -1))
            events.append((i[1], 1))

        events.sort()

        res = []
        cur_sum = 0
        start = 0
        for x, operant in events:
            operant = -operant
            cur_sum += operant
            if cur_sum == 2:
                start = x
            elif cur_sum == 1 and operant == -1:
                res.append([start, x])

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.intervalIntersection_my([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
    print(sol.intervalIntersection_leet([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
    print(sol.intervalIntersection_my([[1, 3]], [[5, 9]]))
    print(sol.intervalIntersection_my([[1, 3], [5, 9]], []))
