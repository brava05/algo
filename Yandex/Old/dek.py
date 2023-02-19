# 70756468
class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
  
    def push_front(self, x):
        if self.size == self.max_n:
            return "error"

        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def push_back(self, x):
        if self.size == self.max_n:
            return "error"

        self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = x
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            return "error"

        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            return "error"
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

def main():
    
    with open("input.txt") as file:
        firstline = file.readline()
        queue = Queue(int(file.readline()))

        for i in range(int(firstline)):
            new_line = file.readline().strip()

            if new_line == "pop_front":
                print(queue.pop_front())
            elif new_line == "pop_back":
                print(queue.pop_back())
            elif new_line[0:10] == "push_front":
                res = queue.push_front(int(new_line[11:]))
                if res == 'error':
                    print(res)
            elif new_line[0:9] == "push_back":
                res = queue.push_back(int(new_line[10:]))
                if res == 'error':
                    print(res)


if __name__ == '__main__':
    main()