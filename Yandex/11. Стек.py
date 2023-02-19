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
    with open("Yandex/input11.txt") as file:
    # with open("input.txt") as file:
        for lineF in file:
            line = lineF.strip().split()

            if line[0] == "push":
                print(stack.push(int(line[1])))
            elif line[0] == "exit":
                print("bye")
                return
            else:
                print(getattr(stack, line[0])())


if __name__ == '__main__':
    main()
