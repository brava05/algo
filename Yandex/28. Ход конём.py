with open("Yandex/input28.txt") as file:
# 293930 при 31 на 34
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())

    prises = [[0]*(m+1) for i in range(n+1)]

    dp = [[0]*(m+1) for i in range(n+1)]
    routs = [[0]*(m+2) for i in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j]+prises[i][j], dp[i][j-1]+prises[i][j])
            if dp[i][j] == dp[i-1][j]+prises[i][j]:
                routs[i][j] = routs[i][j] + routs[i-1][j]
            else:
                routs[i][j] = routs[i][j] + routs[i][j-1]
            if i == 1 and j == 1:
                routs[i][j] = 0
    print(dp[n][m])
    print(routs[n][m])