# with open("Yandex/input.txt") as file:
# with open("input.txt") as file:
    # n = int(file.readline())
    # line = file.readline().strip()
file = open('Yandex/input.txt', 'r', encoding='utf8')
i = 0
for lineF in file:
    
    if i == 0:
        n = int(lineF.strip())
        i = 1
    elif i == 1:
        line = lineF.strip()
        i = 2

maxCount = 0

for left in range(len(line)):
    left_letter = line[left]

    right = left+1
    ostZamen = n
    while True:

        if right == len(line):
            break

        right_letter = line[right]
        if right_letter == left_letter:
            
            right += 1
        else:
            if ostZamen == 0:
                break
            else:
                ostZamen -= 1
                
                right += 1

    maxCount = max(maxCount, right - left)

print(maxCount)
