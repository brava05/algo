with open("Yandex/input9.txt") as file:
# with open("input.txt") as file:
    n, m, k = map(int, file.readline().split())
    for i in range(n):
        list_m = list(map(int, file.readline().split()))
        print(list_m)

print(str(n)+" "+str(m)+" "+str(k))
        