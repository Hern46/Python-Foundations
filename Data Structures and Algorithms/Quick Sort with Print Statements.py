def quick_sort(arr):
    print(f'arr is {arr}')
    quick_sort_helper(arr, 0, len(arr)-1)

def quick_sort_helper(arr, first, last):
    print(f'first is {first}')
    print(f'last is {last}')
    if first < last:

        splitpoint = partition(arr, first, last)
        print(f'splitpoint is {splitpoint}')
        quick_sort_helper(arr, first, splitpoint-1)
        quick_sort_helper(arr, splitpoint+1, last)

def partition(arr, first, last):
    pivot = arr[first]
    print(f'pivot is {pivot}')

    leftmark = first+1
    rightmark = last
    print(f'leftmark is {leftmark}')
    print(f'rightmark is {rightmark}')

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1
            print(f'arr at index {leftmark - 1} was {arr[leftmark-1]}, which was <= the pivot value of {pivot}.')
            print(f'leftmark is now {leftmark}')
        if leftmark < len(arr):
            print(f'arr at {leftmark} is {arr[leftmark]}. pivot is {pivot}. rightmark is {rightmark}.')
        while leftmark <= rightmark and arr[rightmark] >= pivot:
            rightmark -= 1
            print(f'arr at index {rightmark + 1} was {arr[rightmark + 1]}, which was >= the pivot value of {pivot}.')
            print(f'rightmark is now {rightmark}')
        if rightmark >= 0:
            print(f'arr at {rightmark} is {arr[rightmark]}. pivot is {pivot}. leftmark is {leftmark}.')
        if rightmark < leftmark:
            print(f'the rightmark is now less than the leftmark. while loop terminated.')
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
            print(f'arr at {leftmark} is now {arr[leftmark]}. arr at {rightmark} is now {arr[rightmark]}.')
            print(f'arr is {arr}')
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    print(f'{arr[first]} swapped places with the pivot, {arr[rightmark]}.')
    print(f'arr is {arr}')

    return rightmark

arr = [8,5,12,10,7,11,6,3,12]

quick_sort(arr)

print(arr)