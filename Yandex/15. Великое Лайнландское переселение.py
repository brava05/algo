
class StackCalc:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        return self.items.pop()

    def back(self):
        if len(self.items) == 0:
            return "error"
        return self.items[-1]


def main():
    stack = StackCalc()
    towns = []
    with open("Yandex/input15.txt") as file:
    # with open("input.txt") as file:
        n = int(file.readline().strip())
        firstline = file.readline().split()

        for ind, value in enumerate(firstline):
            # хранить будем в виде тапла 
            #первое значение само значение из данных
            # второе куда переселится
            # все таклы вкладываем в лист towns
            # в стеке храним значения которые еще не нашли куда переселяться в виде индекса и значения

            value = int(value)
            towns.append((ind, -1))

            while True:
                last = stack.back()
                if last == "error":
                    break
                lastInd, lastVal = last
                if lastVal <= value:
                    break

                towns[lastInd] = (lastInd, ind)
                stack.pop()

            stack.push((ind, value))

        for tup in towns:
            _, target = tup
            print(target, end=" ")


if __name__ == '__main__':
    main()
