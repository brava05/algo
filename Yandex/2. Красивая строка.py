# file = open('Yandex/input2.txt', 'r', encoding='utf8')
file = open('input.txt', 'r', encoding='utf8')
i = 0
for lineF in file:
    
    if i == 0:
        n = int(lineF.strip())
        i = 1
    elif i == 1:
        line = lineF.strip()
        i = 2

maxCount = 0

for ch in range(ord("a"), ord("z")+1):
    letter = chr(ch)

    right = 0
    left = 0
    ostZamen = n
    while True:
        # left_letter = line[left]

        if right == len(line):
            maxCount = max(maxCount, right - left)
            break

        right_letter = line[right]
        if right_letter == letter:
            right += 1
        else:
            if ostZamen <= 0:
                maxCount = max(maxCount, right - left)

                # будем двигать левый
                if line[left] != letter:
                    ostZamen += 1
                left += 1
            else:
                ostZamen -= 1
                right += 1
        

print(maxCount)
