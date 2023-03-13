# В первой строке входных данных находится количество учеников в классе 2 ≤ N ≤ 109. Во второй строке — количество подготовленных для контрольной вариантов заданий 2 ≤ K ≤ N. В третьей строке — номер ряда, на который уже сел Петя, в четвёртой — цифра 1, если он сел на правое место, и 2, если на левое.
with open("Yandex/input4_5.txt") as file:
# with open("input.txt") as file:
    n = int(file.readline().strip())
    k = int(file.readline().strip())
    row = int(file.readline().strip())
    sit = int(file.readline().strip())

    KolRyadovNado = k//2
    KolRyadovSzadi = n//2+(n%2)*2-row
    mesto = 2*(row-1) + sit
    ostUchenikov = n - mesto
    if k%2 == 0:
        newSit = sit
    else:
        newSit = 3 - sit
        # KolRyadovNado += 1
    
    if ostUchenikov > k:
        print(f'{row+KolRyadovNado} {newSit}')
    else:
        # сзади мест не хватило
        if mesto <= k:
            print(-1)
        else:
            print(f'{row-KolRyadovNado} {newSit}')

# # почему то четвертый вариант 
# 11
# 5
# 3
# 2
# не принимает ответ 6 1