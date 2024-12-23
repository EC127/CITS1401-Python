def dec_trend(data):
    max = data[0]
    result=[]
    result.append(max)
    for num in data:
        if num == max:
            continue
        elif num < max:
            result.append(num)
            max = num
        else:
            continue
    return result

        