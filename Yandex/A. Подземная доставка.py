class Stack:

    def __init__(self):
        self.items = []
        self.dict_of_good = {}

    def add(self, item, good):
        self.items.append((item, good))
        self.dict_of_good[good] = self.dict_of_good.get(good, 0)+item
        return "ok"

    def get(self, good):
        return self.dict_of_good.get(good, 0)

    def delete(self, x):
        if len(self.items) == 0:
            return "error"
        
        left = x
        while left > 0:
            # tup = self.items[-1]
            tup = self.items.pop()
            kol, good = tup
            self.dict_of_good[good] = self.dict_of_good.get(good, 0) - kol
            if kol <= left:
                # не хватило
                left = left - kol
            else:
                # осталось вернуть
                self.add(kol - left, good)
                left = 0

    def size(self):
        return len(self.items)


def main():
    stack = Stack()
    with open("Yandex/inputA.txt") as file:
    # with open("input.txt") as file:
        n = int(file.readline().strip())
    
        for i in range(n):
            line = file.readline().strip().split()

            if line[0] == "add":
                stack.add(int(line[1]), line[2])
            elif line[0] == "delete":
                stack.delete(int(line[1]))
            elif line[0] == "get":
                print(stack.get(line[1]))
            

if __name__ == '__main__':
    main()
