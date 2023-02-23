def search_smoller(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)-1
    mid = 0
    while left<right:
        mid = (left+right)//2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid+1

    if nums[left] < target:
        return left
    else:
        return left-1


def main():
    with open("Yandex/input3.txt") as file:
    # with open("input.txt") as file:
        n = int(file.readline().strip())
        nomera = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        nomera_k = list(map(int, file.readline().strip().split()))

        nomera = sorted(set(nomera))
        res = []
        for min_nomer in nomera_k:
            ind = search_smoller(nomera, min_nomer)
            print(ind+1)
            

if __name__ == '__main__':
    main()
