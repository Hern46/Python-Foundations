def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentval = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > currentval:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = currentval

    return arr

arr = [9,5,8,1,77]
print(insertion_sort(arr))