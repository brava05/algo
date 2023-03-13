with open("Yandex/input28.txt") as file:
# 293930 при 31 на 34
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())
    dp = [[0]*(m+1) for i in range(n+1)]
    
    dp[1][1] = 1
    di = [2, 1]
    dj = [1, 2]
    for i in range(2, n+1):
        for j in range(m+1):
            # for a in range(0, 2):
            dp[i][j] = (0 if (j-2 <0) else dp[i-1][j-2]) + (0 if (i-2 <0) else dp[i-2][j-1])
    print(dp[n][m])