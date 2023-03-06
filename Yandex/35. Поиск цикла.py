def dfs(graf, visited, now):
    global yes
    global color_dict
    # if not now in visited:
    #     visited.append(now)
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

with open("Yandex/input35.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())

    graf = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        tek_list = list(map(int, file.readline().strip().split()))
        for j, val in enumerate(tek_list):
            if val == 0:
                continue
            if not j+1 in graf[i]:
                graf[i].append(j+1)

    print(graf)
    visited = []
    color_dict = {}
    color_dict[1] = 1
    yes = 0
    dfs(graf, visited, 1)
    # print("YES" if yes > 0 else "NO")
    if yes > 0:
        print("YES")
        res = []
        for i, color in color_dict.items():
            if color == 1:
                res.append(i)
        # visited.sort()
        print(len(res))
        print(*res)
    else:
        print("NO")

    