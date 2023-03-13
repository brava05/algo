
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

def get_number(i, j, m):
    return j+m*(i-1)

with open("Yandex/inputE.txt") as file:
# with open("input.txt") as file:
    n, m = map(int, file.readline().strip().split())

    graf = [[1]*(m+1) for i in range(n+1)]
    
    for i in range(1, n+1):
        tek_list = list(file.readline().strip())
        for j, val in enumerate(tek_list):
            if val == "X":
                continue
            graf[n-i+1][j+1] = 0

    # print(graf)

    di = [0,1,1,1,1]
    dj = [-1,-1,0,1,0]

    new_graf = [[] for _ in range(n*m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if graf[i][j] == 1:
                continue
            
            for a in range(5):
                for c in range(1, max(n,m)):
                    teki = i+di[a]*c
                    tekj = j+dj[a]*c
                    if teki < 1 or teki > n:
                        break
                    if tekj < 1 or tekj > m:
                        break
                    if graf[teki][tekj] == 1:
                        break
                    old = j+m*(i-1)
                    new = tekj+m*(teki-1)
                    if not new in new_graf[old]:
                        new_graf[old].append(new)
                    if not old in new_graf[new]:
                        new_graf[new].append(old)

    print(new_graf)

    first_j, first_i = map(int, file.readline().strip().split())
    goal_j, goal_i = map(int, file.readline().strip().split())
    
    first = get_number(first_i, first_j, m)
    goal = get_number(goal_i, goal_j, m)
    visited = {}
    res = bfs(new_graf, visited, first, goal)
    if res is None:
        print(-1)
    else:
        # print(*res)
        print(len(res)-1)