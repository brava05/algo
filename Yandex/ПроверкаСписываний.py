def onlyLetters(line):
    ans = []
    for c in line:
        if c.isalpha() or c.isdigit() or c == " ":
            ans.append(c)
        else:
            ans.append(" ")
    return ''.join(ans)

def isCorrect(word, stDigit):
    if word.isdigit():
        return False
    if not word[0].isDigit() or stDigit:
        return True

    return False

fin = open('input.txt', 'r')
# множество ключевых слов
keyWords = set()
# переменные чувтсвительности к регистру и возможности начинать с цифр
n, caseSens, stDigit = fin.readline().strip().split()
n = int(n)
caseSens = caseSens == 'yes'
stDigit = stDigit == 'yes'

for _ in range(n):
    keyWord = fin.readline().strip()
    if not caseSens:
        keyWord = keyWord.lower()
    keyWords.add(keyWord)
# словарь для количества вхождений
cntPosIds = {}

# счетчик слов
wordNumber = 0
# по всем строкам текст
for line in fin.readlines():

    # заменяем все запрещенные символы на пробелы
    line = onlyLetters(line.strip())

    # нарезаем строку на слова
    words = line.split() 
    # для каждого слова проверяем не ключевое ли оно
    for word in words:
        if not caseSens:
            word = word.lower()
        if word in keyWords:
            continue
        # если ключевое, проеряем что оно корректно 
        if isCorrect(word, stDigit):
            wordNumber += 1
            if word not in cntPosIds:
                # если встретилось впервые, то запоминаем порядоковый номер слова
                cntPosIds[word] = [0, wordNumber]
            # если ок то увеличиваем счетчик на 1
            cntPosIds[word][0] += 1

# по вловарю вхождений находим максимальное вхождение
bestWord = ''
maxCntPos = [0, 0]
for word in cntPosIds:
    if cntPosIds[word][0] > maxCntPos[0]:
        maxCntPos = cntPosIds[word]
        bestWord = word
    # из равного вхождения берем то которое было раньше
    if cntPosIds[word][0] == maxCntPos[0] and cntPosIds[word][1] < maxCntPos[1]:
        maxCntPos = cntPosIds[word]
        bestWord = word
    


