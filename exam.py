def stringList(lst) :
    result=[]
    term = ''
    for item in lst:
        if type(item) == type(10) or type(item) == type(4.1):
            item = str(item)
        if item == True:
            item = 'True'
        if item == False:
            item = 'False'
        term = term+item
        result.append(term)
    return result[-1]
    