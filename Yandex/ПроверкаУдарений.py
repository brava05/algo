n = int(input())
dictLower = {}
for _ in range(n):
    s = input()
    slower = s.lower()
    if slower not in dictLower:
        dictLower[slower] = set()
    dictLower[slower].add(s)

# проверяем есть ли слово в словаре, то сравниеам с сетом
# иначе проверяем количество ударений в слове их должно быть ровно 1

text = input()
mistakes = 0
for word in text.split():
    wordLower = word.lower()
    if wordLower in dictLower:
        if word not in dictLower[wordLower]:
            mistakes += 1
    else:
        stresses = 0
        for letter in word:
            if letter.isupper():
                stresses += 1

        if stresses != 1:
            mistakes += 1
            
print(mistakes)
