def dfs(graf, visited, now):
    global bad
    global color_dict
    if not now in visited:
        visited.append(now)
    for neib in graf[now]:
        if not neib in visited:
            if color_dict.get(neib, 0) == color_dict.get(now, 0):
                bad += 1
            else:
                color_dict[neib] = 3 - color_dict.get(now, 0)
            dfs(graf, visited, neib)

with open("Yandex/input33.txt") as file:
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
    color_dict = {}
    color_dict[1] = 1
    bad = 0
    dfs(graf, visited, 1)

    # print(bad)
    print("YES" if bad == 0 else "NO")
    # print(color_dict)
