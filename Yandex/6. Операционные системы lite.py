with open("Yandex/input6.txt") as file:
# with open("input.txt") as file:
    m = int(file.readline().strip())
    n = int(file.readline().strip())
    list_OS = []
    for i in range(n):
        # start, end = tuple(map(int, file.readline().strip().split()))
        tek_OS = list(map(int, file.readline().strip().split()))
        print(tek_OS)
        i = 0
        while i < len(list_OS): 
            OS = list_OS[i]
            if OS[0] <= tek_OS[1] and OS[1] >= tek_OS[0]:
                list_OS.pop(i)
            else:
                i += 1

        list_OS.append(tek_OS)

        print(len(list_OS))
            
