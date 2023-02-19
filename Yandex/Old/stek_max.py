class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        if self.max_items:
            self.max_items.append(max(self.max_items[-1], item))
        else:
            self.max_items.append(item)

        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        self.max_items.pop()
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if len(self.items) == 0:
            return "None"
        return self.max_items[-1]

def main():
    stack = StackMaxEffective()
    with open("input.txt") as file:
        firstline = file.readline()

        for i in range(int(firstline)):
            new_line = file.readline().strip()
            # print(new_line)

            if new_line == "get_max":
                print(stack.get_max())
            if new_line == "pop":
                res = stack.pop()
                if res == 'error':
                    print(res)
            if new_line[0:4] == "push":
                stack.push(int(new_line[5:]))


if __name__ == '__main__':
    main()