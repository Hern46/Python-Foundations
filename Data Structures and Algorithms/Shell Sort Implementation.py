def shell_sort(arr):

    sublist_count = len(arr)//2

    while sublist_count > 0:
        for n in range(sublist_count):
            gap_insertion_sort(arr, n, sublist_count)

        sublist_count = sublist_count//2

    return arr

def gap_insertion_sort(arr, n, gap):
    for i in range(n+gap, len(arr), gap):
        currentval = arr[i]
        pos = i

        while pos >= gap and arr[pos-gap] > currentval:
            arr[pos] = arr[pos-gap]
            pos = pos-gap

        arr[pos] = currentval

arr = [55,6,-9393,4,0,99,100,15]
print(shell_sort(arr))
