with open("Yandex/input5.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())
    prev = 0
    res = 0
    for i in range(n):
        k = int(file.readline().strip())
        if i == 0:
            prev = k
            continue
        res = res + min(k, prev)
        prev = k

print(res)