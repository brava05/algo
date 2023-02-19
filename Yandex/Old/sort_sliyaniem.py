def merge_rab(arr, lf=0, rg=0):
    if len(arr) == 1:  # базовый случай рекурсии
        return arr
    left = merge_rab(arr[0:len(arr)//2])
    right = merge_rab(arr[len(arr)//2:len(arr)])
    result = [None]*len(arr)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right): 
    # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]: 
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left): 
        result[k] = left[l] # перенеси оставшиеся элементы left в result
        l += 1
        k += 1  
    while r < len(right): 
        result[k] = right[r] # перенеси оставшиеся элементы right в result
        r += 1
        k += 1
  
    return result


def main():
    c = [1, 4, 2, 10, 1, 2]
    arr2 = merge_rab(c, 0 , 6)
    print(*arr2)

if __name__ == '__main__':
    main()