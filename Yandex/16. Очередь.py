class MyQueue:

    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.alsize = 0
        
    def is_empty(self):
        return self.alsize == 0
        
    def push(self, x):
        if self.alsize == self.max_size:
            return 'error'
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size
        self.alsize += 1
        return "ok"

    def pop(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = 0
        self.head = (self.head + 1) % self.max_size
        self.alsize -= 1
        return x

    def front(self):
        if self.is_empty():
            return 'error'
        return(self.queue[self.head])

    def size(self):
        return self.alsize

    def clear(self):
        self.queue = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.alsize = 0
        return "ok"

def main():
    stack = MyQueue(100)
    with open("Yandex/input16.txt") as file:
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
