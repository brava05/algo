class StackCalc:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return "ok"

    def pop(self):
        if len(self.items) == 0:
            return "error"
        return self.items.pop()

    def back(self):
        if len(self.items) == 0:
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def exit(self):
        return "bye"

    def clear(self):
        self.items.clear()
        return "ok"


def main():
    stack = StackCalc()
    with open("Yandex/input14.txt") as file:
    # with open("input.txt") as file:
        n = int(file.readline().strip())
        k = list(map(int, file.readline().strip().split()))
        tek_need = 1
        for number in k:
            stack.push(number)

            while True:
                if stack.size() > 0 and stack.back() == tek_need:
                    tek_need += 1
                    stack.pop()
                else:
                    break
        
        if tek_need == n+1:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
