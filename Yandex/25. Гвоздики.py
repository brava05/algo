# В дощечке в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. Требуется соединить некоторые пары гвоздиков ниточками так, чтобы к каждому гвоздику была привязана хотя бы одна ниточка, а суммарная длина всех ниточек была минимальна
with open("Yandex/input25.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())
    k = list(map(int, file.readline().strip().split()))
    k.sort()
    print(k)

    dp = [0]*(n+1)

    dp[1] = 100000
    for i in range(2, n+1):
        dp[i] = min(dp[i-1], dp[i-2])+(k[i-1]-k[i-2])
    print(dp[n])