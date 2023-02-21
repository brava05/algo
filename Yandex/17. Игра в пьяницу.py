
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
        self.queue[self.head] = None
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

def FirstWin(val1, val2):
    if val1 == 0 and val2 == 9:
        return True
    if val1 == 9 and val2 == 0:
        return False
    return(val1>val2)
    

def main():
    Queue1 = MyQueue(20)
    Queue2 = MyQueue(20)
    # with open("Yandex/input17.txt") as file:
    with open("input.txt") as file:
        line1 = file.readline().strip().split()
        line2 = file.readline().strip().split()
        for i in range(5):
            Queue1.push(int(line1[i]))
            Queue2.push(int(line2[i]))

        for i in range(1000000):
            card1 = Queue1.pop()
            card2 = Queue2.pop()

            if FirstWin(card1, card2):
                Winner = Queue1
            else:
                Winner = Queue2

            Winner.push(card1)
            Winner.push(card2)

            if Queue1.size() == 0:
                return("second "+str(i+1))
            if Queue2.size() == 0:
                return("first "+str(i+1))

        return("botva")


if __name__ == '__main__':
    res = main()
    print(res)
