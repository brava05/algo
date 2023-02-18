with open("Yandex/input.txt") as file:
    n = int(file.readline())
    min_x = None
    min_y = None
    max_x = 0
    max_y = 0
    for i in range(n):
        x, y = map(int, file.readline().split())
        if min_x == None:
            min_x = x
        if min_y == None:
            min_y = y
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

print(str(min_x)+" "+str(min_y)+" "+str(max_x)+" "+str(max_y))
        