class Solution:
    # https://www.youtube.com/watch?v=8-xzy50m-dY&t=753s
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        comb = [i for i in range(1, k+1)]
        while True:
            res.append(comb.copy())
            m = -1
            for i in range(k-1, -1, -1):
                if comb[i] <= n-k+i:
                    m = i
                    comb[i] += 1
                    break
            if m == -1:
                break
            for i in range(m+1, k):
                comb[i] = comb[i-1]+1

        return res

if __name__ == '__main__':
    sol = Solution()

    print(sol.combine(5, 3))