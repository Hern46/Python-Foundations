import random
coin_arr = [1]*7
coin_arr.append(random.randint(2,3))
random.shuffle(coin_arr)
#print(coin_arr)

def coin_and_scale(arr,count=0):
    print(arr)
    print(count)
    mid = len(arr)//2
    print(mid)
    if len(arr) > 2:
        for i in range(1,len(coin_arr)):
            if coin_arr[i-1] > coin_arr[i]:
                count += 1
                if i-1 < mid:
                    return coin_and_scale(arr[:mid], count)
                else:
                    return coin_and_scale(arr[mid:], count)
    else:
        print('hey')
        count += 1
        print(count)

    return (count, max(arr))

#print(coin_and_scale(coin_arr))

def coin2(arr, count=0, sum1=0, sum2=0):
    print(arr)
    if len(arr) > 2:
        mid = len(arr)//2

        for coin in arr[:mid]:
            sum1 += coin

        for coin in arr[mid:]:
            sum2 += coin

        if sum1 > sum2:
            count += 1
            return coin2(arr[:mid], count)
        else:
            count += 1
            return coin2(arr[mid:], count)

    else:
        count += 1

    return (count, max(arr))

print(coin2(coin_arr))
