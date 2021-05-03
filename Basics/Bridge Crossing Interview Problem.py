
traveler_speeds = [1,2,5,10]

def bridge2(traveler_speeds, max_list=[], min_list=[]):

    if traveler_speeds != []:

        min_list.append(traveler_speeds.pop(traveler_speeds.index(min(traveler_speeds))))
        max_list.append(traveler_speeds.pop(traveler_speeds.index(min(traveler_speeds))))

        bridge2(traveler_speeds, max_list, min_list)

    time = 0
    for val in max_list:
        time += val

    return time + 2*min(max_list) + min(min_list)

print(bridge2(traveler_speeds))





