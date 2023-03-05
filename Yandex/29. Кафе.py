with open("Yandex/input29.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())
    prises = []
    wast_kupon = 0
    kupons_days = []
    for i in range(1, n+1):
        prises.append(int(file.readline().strip()))

    # print(prises)

    dp = [[10000]*(n+1) for i in range(n+1)]
    # print(dp)
    dp[0][0] = 0
    routs = [[[]]*(n+2) for i in range(n+2)]
    for i in range(1, n+1):
        price = prises[i-1]
        for j in range(0, n):
            # j это количество купотонов а i это номер дня
            if price > 100:
                kupon = 1
            else:
                kupon = 0

            if dp[i-1][j]+price <= dp[i-1][j+1]:
                # в этот день платим
                dp[i][j+kupon] = dp[i-1][j]+price

                routs[i][j] = routs[i-1][j].copy()

            else:
                if dp[i-1][j+1] != 10000:
                    # расходуем купон
                    dp[i][j] = dp[i-1][j+1]

                    last_route = routs[i-1][j+1].copy()
                    last_route.append(i)
                    routs[i][j] = last_route

    res = min(dp[n])  
    # print(dp)      
    print(res)
    last_day_list = dp[n]
    last_day_list.reverse()
    kupons_left = last_day_list.index(res)-n
    # kupons_left = dp[n].index(res)

    # print(kupons_left, end="")
    # print(" ", end="")
    rout = routs[n][kupons_left]
    print(*[kupons_left, len(rout)])
    
    # print(len(rout))
    for i in rout:
        print(i)