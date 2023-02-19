class Deque:

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def push_front(self, x):
        if self.__size == self.max_n:
            return "error"

        self.queue[self.__tail] = x
        self.__tail = (self.__tail + 1) % self.max_n
        self.__size += 1

    def push_back(self, x):
        if self.__size == self.max_n:
            return "error"

        self.__head = (self.__head - 1) % self.max_n
        self.queue[self.__head] = x
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            return "error"

        x = self.queue[self.__head]
        self.queue[self.__head] = None
        self.__head = (self.__head + 1) % self.max_n
        self.__size -= 1
        return x

    def back(self):
        if self.is_empty():
            return "error"

        return self.queue[self.__head]

    def pop_front(self):
        if self.is_empty():
            return "error"
        x = self.queue[self.__tail - 1]
        self.queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.max_n
        self.__size -= 1
        return x

    def front(self):
        if self.is_empty():
            return "error"
        return self.queue[self.__tail - 1]

    def size(self):
        return self.__size

    def clear(self):
        self.queue = [None] * self.max_n
        self.__head = 0
        self.__tail = 0
        self.__size = 0
        return "ok"

def main():
    stack = Deque(100)
    # with open("Yandex/input18.txt") as file:
    with open("input.txt") as file:
        for lineF in file:
            line = lineF.strip().split()

            if line[0] == "push_front":
                print(stack.push_front(int(line[1])))
            elif line[0] == "push_back":
                print(stack.push_back(int(line[1])))
            elif line[0] == "exit":
                print("bye")
                return
            else:
                print(getattr(stack, line[0])())


if __name__ == '__main__':
    main()
