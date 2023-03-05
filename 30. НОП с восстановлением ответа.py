with open("Yandex/input30_2.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())
    line1 = ["#"]
    line1.extend(file.readline().strip().split())
    m = int(file.readline().strip())
    line2 = [" "]
    line2.extend(file.readline().strip().split())

    print(line1)
    print(line2)

    dp = [[0]*(n+1) for i in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        letter_i = line1[i]
        
        for j in range(1, m+1):
            letter_j = line2[j]

            if letter_i == letter_j:
                # буквы совпали берем значение dp по диагонали
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    print(dp[n][m]) 
    print(dp) 

    # восстановление ответа
    res = []
    i = n
    j = m
    while j > 0:
        if dp[i][j] == dp[i-1][j-1]+1:
            # буквы совпали берем значение dp по диагонали
            res.append(line1[i])
            i -= 1
            j -= 1
        else:
            j -= 1

    res.reverse()
    print(*res)