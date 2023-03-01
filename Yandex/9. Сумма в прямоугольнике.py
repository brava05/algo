with open("Yandex/input9.txt") as file:
# with open("input.txt") as file:
    n, m, k = map(int, file.readline().split())
    sums = [ [0]*m for i in range(n)]
    for i in range(n):
        list_m = list(map(int, file.readline().split()))
        
        for j in range(m):
            if i == 0 and j ==0:
               sums[i][j] = list_m[j]
               continue
            if i == 0:
                sums[i][j] = sums[i][j-1] + list_m[j]
            elif j == 0:
                sums[i][j] = sums[i-1][j] + list_m[j]
            else:
                sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + list_m[j]

        # print(list_m)
    # print(sums)
    for ik in range(k):
        x1, y1, x2, y2 = map(int, file.readline().split())
        sumx2y2 = sums[x2-1][y2-1]
        
        if x1 == 1 and y1 == 1:
            sumx1y1 = 0
        else:
            sumx1y1 = sums[x1-2][y1-2]
        
        if y1 == 1:
            sum_left = 0
            sumx1y1 = 0
        else:
            sum_left = sums[x2-1][y1-2]

        if x1==1:
            sum_up = 0
            sumx1y1 = 0
        else:    
            sum_up = sums[x1-2][y2-1]

        print(sumx2y2-sum_left-sum_up+sumx1y1)


# print(str(n)+" "+str(m)+" "+str(k))
        