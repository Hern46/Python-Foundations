
def pair_sum(arr, k):
    arr2 = []
    k_div_2_arr = []
    for j in range(len(arr)):
        if arr[j] == k/2:
            k_div_2_arr.append(arr[j])
        elif k - arr[j] >= 0 and k - arr[j] in arr and k - arr[j] != arr[j]:
            arr2.append((k - arr[j], arr[j]))
    for (a,b) in arr2:
        if (b,a) in arr2:
            arr2.remove((b,a))

    arr_set = set(arr2)
    if len(k_div_2_arr) >= 2:
        arr_set.add((k_div_2_arr[0], k_div_2_arr[1]))
    return arr_set, len(arr_set)

print(pair_sum([4,2,1,10,9,11,3,15,-1,88,13,-9,-2,-8,0,4,4,4,4,30,-16,15, 16, 74, 60, 74, 60, 22,8,33,7,7,7,-7,-7,-14,28,14,0,14,33,17,18], 14))
