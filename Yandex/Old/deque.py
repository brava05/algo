# 70898302

class QueueOverFlowError(Exception):

    def __str__(self):
        return 'error'


class QueueEmptyError(Exception):

    def __str__(self):
        return 'error'


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
            return QueueOverFlowError()

        self.queue[self.__tail] = x
        self.__tail = (self.__tail + 1) % self.max_n
        self.__size += 1

    def push_back(self, x):
        if self.__size == self.max_n:
            return QueueOverFlowError()

        self.__head = (self.__head - 1) % self.max_n
        self.queue[self.__head] = x
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            return QueueEmptyError()

        x = self.queue[self.__head]
        self.queue[self.__head] = None
        self.__head = (self.__head + 1) % self.max_n
        self.__size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            return QueueEmptyError()
        x = self.queue[self.__tail - 1]
        self.queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.max_n
        self.__size -= 1
        return x


def main():
    with open("input.txt") as file:
        firstline = file.readline()
        queue = Deque(int(file.readline()))

        for i in range(int(firstline)):
            new_line = file.readline().strip()
            space = new_line.find(' ')
            if space >= 0:
                res = getattr(queue, new_line[0:space])(
                    int(new_line[space+1:])
                    )
                if res == 'error':
                    print(res)
            else:
                print(getattr(queue, new_line)())


if __name__ == '__main__':
    main()
