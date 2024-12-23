def sortVehicles(vehicle):
    list2 = []
    for key in vehicle:
        list= []
        list.append(key)
        list = list + vehicle[key]
        list2.append(list)
    #print(list2)
    list2 = sorted(list2, key=lambda list2: (-list2[3]))
    #print(list2)
    result = []
    for item in list2:
        term = []
        term.append(item[1])
        term.append(item[0])
        term.append(item[3])
        term.append(item[4])
        result.append(term)
    return result