def dfs(graf, visited, now, tek_comp):
    if not now in visited:
        visited.append(now)
        tek_comp.append(now)
    for neib in graf[now]:
        if not neib in visited:
            dfs(graf, visited, neib, tek_comp)

with open("Yandex/input32.txt") as file:
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())

    graf = [[] for _ in range(n+1)]
    for i in range(m):
        tek_list = list(map(int, file.readline().strip().split()))
        if not tek_list[1] in graf[tek_list[0]]:
            graf[tek_list[0]].append(tek_list[1])
        if not tek_list[0] in graf[tek_list[1]]:
            graf[tek_list[1]].append(tek_list[0])

    # print(graf)
    visited = []
    comonents = []
    for now in range(1, n+1):
        tek_comp = []
        if not now in visited:
            dfs(graf, visited, now, tek_comp)
            comonents.append(tek_comp)

    print(len(comonents))
    for tek_comp in comonents:
        print(len(tek_comp))
        print(*tek_comp)
