with open("Yandex/input10.txt") as file:
# with open("input.txt") as file:
    line = file.readline().strip()

    letters = {}
    for ch in range(ord("a"), ord("z")+1):
        letters[chr(ch)] = 0

    lenl = len(line)
    for i in range(lenl):
        letter = line[i]
        letters[letter] = letters[letter] + (i+1)*(lenl-i)

    for letter, n in letters.items():
        if n == 0:
            continue
        print(f"{letter}: {n}")     