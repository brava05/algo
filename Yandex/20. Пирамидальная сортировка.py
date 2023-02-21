class Heap:

    def __init__(self):
        self.list = []

    def Insert(self, x):
        self.list.append(x)
        pos = len(self.list)-1
        while pos > 0 and self.list[pos] > self.list[(pos - 1)//2]:
            self.list[pos], self.list[(pos - 1)//2] = self.list[(pos - 1)//2], self.list[pos] 
            pos = (pos - 1)//2


    def Extract(self):

        if len(self.list) == 0:
            return "error"

        x = self.list[0]
        self.list[0] = self.list[len(self.list) - 1]
        pos = 0
        while 2*pos + 1 < len(self.list) - 1:
            if self.list[2*pos + 1] > self.list[2*pos + 2]:
                max_ind = 2*pos + 1
            else:
                max_ind = 2*pos + 2
            
            if self.list[max_ind] > self.list[pos]:
                self.list[max_ind], self.list[pos] = self.list[pos], self.list[max_ind]
                pos = max_ind
            else:
                break
        self.list.pop()
        return x


def main():
    heap = Heap()
    with open("Yandex/input20.txt") as file:
    # with open("input.txt") as file:
        n = int(file.readline().strip())
        line = file.readline().strip().split()
    
    for i in range(n):
        heap.Insert(int(line[i]))

    for i in range(n):
        line[len(line)-i-1] = heap.Extract()

    print(*line)

if __name__ == '__main__':
    main()
