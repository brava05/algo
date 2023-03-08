
def bfs(graf, visited, now, goal):

    if now == goal:
        return[now]
        
    que = [(now, [now])]
    visited[now] = True

    while len(que):
        current, path = que.pop(0)
        for neig in graf[current]:
            if neig not in visited:
                if neig == goal:
                    path.append(neig)
                    return (path)
                else:
                    new_path = list(path)
                    new_path.append(neig)
                    que.append((neig, new_path))
                visited[neig] = True
    
    return None


with open("Yandex/input36.txt") as file:
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

    first, goal = map(int, file.readline().strip().split())
    # print(graf)

    visited = {}
    res = bfs(graf, visited, first, goal)
    if res is None:
        print(-1)
    else:
        # print(*res)
        print(len(res)-1)