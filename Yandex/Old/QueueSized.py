class MyQueueSized:

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

    def pop(self):
        if self.is_empty():
            return 'None'
        x = self.queue[self.head]
        self.queue[self.head] = 0
        self.head = (self.head + 1) % self.max_size
        self.alsize -= 1
        return x

    def peek(self):
        if self.is_empty():
            return 'None'
        return(self.queue[self.head])

    def size(self):
        return self.alsize


def main():
    with open('input.txt') as file:
        first_line = file.readline()
        second_line = file.readline()
        my_queue = MyQueueSized(int(second_line))
        for i in range(int(first_line)):
            new_line = file.readline().strip()
            # probel = new_line.find(' ')
            # if probel > -1:
            #     res = getattr(my_queue, new_line[0:probel])(int(new_line[probel+1:]))
            # else:
            #     res = getattr(my_queue, new_line)()
            # if res != None:
                # print(res)
            if new_line == "peek":
                print(my_queue.peek())
            elif new_line == "size":
                print(my_queue.size())
            elif new_line == "pop":
                print(my_queue.pop())
            elif new_line[0:4] == "push":
                res = my_queue.push(int(new_line[5:]))
                if res == 'error':
                    print(res)


if __name__ == "__main__":
    main()