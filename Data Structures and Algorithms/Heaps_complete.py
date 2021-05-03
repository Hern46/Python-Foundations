import random
import math

rand_arr = []

for x in range(random.randint(1,100)):
    rand_arr.append(random.randint(1,100))

def is_heap(heap):
    for x in range((len(heap)-1)//2):
        try:
            if heap[x] < heap[x * 2 + 1] or heap[x] < heap[x * 2 + 2]:
                return False
        except IndexError:
            continue
    return True

def heapify_helper(arr, node_index):
    parent_index_increment = 0 # If it's a left child, increment = 0. If it's a right child, increment = -1
    node_index_increment = 1

    if node_index >= 1:

        if node_index % 2 == 0: # This would occur for right children.
            parent_index_increment = -1
            node_index_increment = 2

            child = max(arr[node_index], arr[node_index - 1])
            if arr[node_index] == child:
                child_index = node_index
            else:
                child_index = node_index - 1

        else: # This would occur for left children. This should only happen once if the first child is a lonely left child.
            child = arr[node_index]
            child_index = node_index

        if child > arr[(node_index // 2) + parent_index_increment]:
            parent = arr[(node_index // 2) + parent_index_increment]
            arr[(node_index // 2) + parent_index_increment] = child
            arr[child_index] = parent

        node_index -= node_index_increment
        heapify_helper(arr, node_index)

    return arr

def heapify(arr):
    '''
    Time complexity is O(n). It is equal to (loops_to_do + 1) * n/2.
    The number of levels in a heap is equal to math.floor(math.log(len(arr), 2)) + 1, where arr is the original array being converted into a heap.
    :param arr: Any array that you wish to convert into a max heap.
    :return: Returns a max heap.
    '''

    loops_to_do = math.floor(math.log(len(arr), 2)) - 1
    node_index = len(arr) - 1

    while loops_to_do >= 0:
        loops_to_do -= 1
        arr = heapify_helper(arr, node_index)

    return arr

def heap_sort(heap, sorted_arr=[]):
    largest = heap.pop(0)
    sorted_arr.insert(0, largest)

    if heap:
        next_ele = heap.pop()
        heap.insert(0, next_ele)
        new_heap = heapify(heap)
        heap_sort(new_heap, sorted_arr)

    return sorted_arr

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def sort(arr):
    created_heap = heapify(arr)
    new_sorted_arr = heap_sort(created_heap)
    return new_sorted_arr


#my_arr = [2,45,98,45,15,74,75,75,23,6]
#print(my_arr)

#heap = heapify(my_arr)

print(rand_arr)
heap = heapify(rand_arr)
print(heap)
print(is_heap(heap))
x = heap_sort(heap)
print(x)
print(is_sorted(x))