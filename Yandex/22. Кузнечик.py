# Длина доски — N клеток. К его сожалению, он умеет прыгать только на 1, 2, …, k клеток вперёд.
# Однажды студентам стало интересно, сколькими способами кузнечик может допрыгать из первой клетки до последней

with open("Yandex/input22.txt") as file:
# with open("input.txt") as file:
    n, k = map(int, file.readline().strip().split())

    dp = [0]*(n+1)
    dp[1] = 1
    dp[0] = 0
    for i in range(2, n+1):
        for j in range(k):
            if i-1-j <0:
                break
            dp[i] = dp[i] + dp[i-1-j]
    print(dp[n])