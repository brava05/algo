def main():
    cifri = (input())
    KOLICH = len(cifri)
    
    all_variants(cifri)
    print(*RESULT) 
 
if __name__ == '__main__':
    main()
 
class Сompeting:
    def __init__(self, name, solved_tasks, penalty):
        self.name = name
        self.solved_tasks = int(solved_tasks)
        self.penalty = int(penalty)
 
    def __lt__(self, second):
        return((-self.solved_tasks, self.penalty, self.name)<(-second.solved_tasks, second.penalty, second.name))
 
def partition(array_p, left, right):
 
    pivot_index = random.randint(left, right-1)
    pivot = array_p[pivot_index]
 
    while right > left:
        while left <= right and array_p[left] < pivot:
            left += 1
        while left <= right and pivot < array_p[right]:
            right -= 1
 
        if left < right:
            array_p[left], array_p[right] = array_p[right], array_p[left]
            left += 1
            if left < right:
                right -= 1
        else:
            break
 
    return left
 
def quicksort(array, left=0, right=None):
 
    if right is None:
        right = len(array)-1
 
    if left >= right:
        return array
 
    if right - left == 1:
        if not array[left] < array[right]:
            array[right], array[left] = array[left], array[right]
        return array
 
    mid = partition(array, left, right)
 
    quicksort(array, left, mid)
    quicksort(array, mid, right)
 
    return array
 
def main():
 
    list_of_compet = []
    with open("input.txt") as file:
        n = int(file.readline())
        for i in range(n):
            name, solved_tasks, penalty = file.readline().split()
            list_of_compet.append(
                Сompeting(name, int(solved_tasks), int(penalty))
                )
 
        print(*(elem.name for elem in quicksort(list_of_compet)), sep = "\n")
 
if __name__ == '__main__':
    main()
