with open("Yandex/input26.txt") as file:
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())

    prises = [[0]*(m+1) for i in range(1)]
    for i in range(1, n+2):
        k = [1000]
        k.extend(list(map(int, file.readline().strip().split())))
        prises.append(k)

    # print(prises)

    dp = [[1000]*(m+1) for i in range(n+1)]
    # dp[0][0] = 0
    # для старта с нуля
    dp[1][0] = 0 
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = min(dp[i-1][j]+prises[i][j], dp[i][j-1]+prises[i][j])
    print(dp[n][m])
    # print(dp)