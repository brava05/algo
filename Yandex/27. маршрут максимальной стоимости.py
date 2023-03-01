with open("Yandex/input27.txt") as file:
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())

    prises = [[0]*(m+1) for i in range(1)]
    for i in range(1, n+2):
        k = [0]
        k.extend(list(map(int, file.readline().strip().split())))
        prises.append(k)

    dp = [[0]*(m+1) for i in range(n+1)]
    routs = [[""]*(m+2) for i in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j]+prises[i][j], dp[i][j-1]+prises[i][j])
            if dp[i][j] == dp[i-1][j]+prises[i][j]:
                routs[i][j] = routs[i-1][j] + "D"
            else:
                routs[i][j] = routs[i][j-1] + "R"
            if i == 1 and j == 1:
                routs[i][j] = ""
    print(dp[n][m])
    print(*list(routs[n][m]))