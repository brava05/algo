# На вход программы поступает сначала число N — количество покупателей в очереди (1 ≤ N ≤ 5000). Далее идет N троек натуральных чисел Ai, Bi, Ci.
# Каждое из этих чисел не превышает 3600. Люди в очереди нумеруются, начиная от кассы.
with open("Yandex/input24_2.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())

    prises = [[4000]*3]*(n+3)
    for i in range(3, n+3):
        k = list(map(int, file.readline().strip().split()))
        prises[i] = k

    # print(prises)

    dp = [0]*(n+3)
    dp[0] = 0
    for i in range(3, n+3):
        dp[i] = min(dp[i-1]+prises[i][0], dp[i-2]+prises[i-1][1], dp[i-3]+prises[i-2][2])
    print(dp[n+2])