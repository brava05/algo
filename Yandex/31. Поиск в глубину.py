def dfs(graf, visited, now):
    if not now in visited:
        visited.append(now)
    for neib in graf[now]:
        if not neib in visited:
            dfs(graf, visited, neib)

with open("Yandex/input31_2.txt") as file:
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
    dfs(graf, visited, 1)

    visited.sort()
    print(len(visited))
    print(*visited)
