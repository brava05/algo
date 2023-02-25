# Имеется калькулятор, который выполняет следующие операции:
# умножить число X на 2;
# умножить число X на 3;
# прибавить к числу X единицу.
# Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.
n = input()
n = int(n)

dp = [0]*(n+1)
prev = [0]*(n+1)
ans = []
# ans.append(1)
dp[1] = 0
for i in range(2, n+1):
    dp[i] = min(dp[i-1] + 1,dp[i//2]+1 if i%2==0  else n, dp[i//3]+1 if i%3==0 else n)
    if dp[i] == dp[i-1] + 1:
        prev[i] = i-1
    elif dp[i] == dp[i//2] + 1 and i%2==0:
        prev[i] = i//2
    else:
        prev[i] = i//3
print(dp[n])

tekInd = n
while tekInd >= 1:
    ans.append(tekInd)
    tekInd = prev[tekInd]

ans.reverse()
print(*ans)