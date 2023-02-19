# 70856138
class StackCalc:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "error"
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def main():
    stack = StackCalc()
    dict_of_operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y}
    with open("input.txt") as file:
        firstline = file.readline().split()

        for elem in firstline:
            if elem in dict_of_operations:
                prev = stack.pop()
                stack.push(dict_of_operations[elem](stack.pop(), prev))
            else:
                stack.push(int(elem))
        print(stack.pop())


if __name__ == '__main__':
    main()
