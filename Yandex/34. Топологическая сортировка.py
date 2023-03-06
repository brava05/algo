def dfs(graf, visited, now):
    global yes
    global color_dict
    global res
    if not now in visited:
        visited.append(now)
    if color_dict.get(now, 0) == 0:
        color_dict[now] = 1
        
    for neib in graf[now]:
        # if not neib in visited:
        if color_dict.get(neib, 0) == 1:
            yes += 1
            return
        dfs(graf, visited, neib)
    
    if yes == 0:
        color_dict[now] = 2

    if not now in res:
        res.append(now)

with open("Yandex/input34_1.txt") as file:
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())

    graf = [[] for _ in range(0, n+1)]
    for i in range(0, m):
        tek_list = list(map(int, file.readline().strip().split()))
        if not tek_list[1] in graf[tek_list[0]]:
            graf[tek_list[0]].append(tek_list[1])

    # print(graf)

    visited = []
    color_dict = {}
    color_dict[1] = 1
    res = []
    yes = 0

    for now in range(1, n+1):
        if not now in visited:
            dfs(graf, visited, now)

    # print(res)
    if yes > 0:
        print("-1")
    else:
        # print("NO")
        res.reverse()
        print(*res)
