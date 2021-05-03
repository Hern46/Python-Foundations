def insertion_sort(arr):
    print(f'arr is {arr}')
    for i in range(1, len(arr)):
        print(f'i is {i}')
        currentval = arr[i]
        pos = i
        print(f'currentval is {currentval}')
        print(f'pos is {pos}')
        while pos > 0 and arr[pos-1] > currentval:
            arr[pos] = arr[pos-1]
            pos -= 1
            print(f'After decrement, pos is {pos}')

        arr[pos] = currentval
        print(f'arr is {arr}')

    return arr

arr = [99,1,0,50,51]
print(insertion_sort(arr))
