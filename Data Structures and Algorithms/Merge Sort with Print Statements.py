def merge_sort(arr):
    print(f'arr is {arr}')
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        print(f'lefthalf is {lefthalf}')
        print(f'righthalf is {righthalf}')
        merge_sort(lefthalf)
        merge_sort(righthalf)
        print(f'lefthalf is {lefthalf}')
        print(f'righthalf is {righthalf}')

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                print(f'lefthalf value was smaller. arr at index {k} was assigned the value {lefthalf[i]}. i is now {i + 1}.')
                i += 1

            else:
                arr[k] = righthalf[j]
                print(f'righthalf value was smaller. arr at index {k} was assigned the value {righthalf[j]}. j is now {j + 1}.')
                j += 1

            k += 1
            print(f'i is now {i}. j is now {j}. k is now {k}.')

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
            print(f'from the lefthalf, arr at index {k-1} was assigned the value {lefthalf[i-1]}. i is now {i} and k is now {k}.')
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
            print(f'from the righthalf, arr at index {k-1} was assigned the value {righthalf[j-1]}. j is now {j} and k is now {k}.')
        print(f'arr is {arr}')

arr = [40,1,22,3]

print(merge_sort(arr))