def selection_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        max_pos = 0
        for i in range(1, n+1):
            if arr[i] > arr[max_pos]:
                max_pos = i

        temp = arr[n]
        arr[n] = arr[max_pos]
        arr[max_pos] = temp

    return arr

arr = [4,1,10,5,8]
print(selection_sort(arr))

