def horse(i, j):
    if i < 0 or j < 0:
        return 0
    if i==1 and j ==1:
        return 1
    return(horse(i-1, j-2) + horse(i-2, j-1))

with open("Yandex/input28.txt") as file:
# 293930 при 31 на 34
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())
    # print(dp[n][m])
    print(horse(n, m))