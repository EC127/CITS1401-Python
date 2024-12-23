def odd_finder(a,b,c,d,e,f,g,h,i,j):
    count = 0
    for elements in [a,b,c,d,e,f,g,h,i,j]:
        if (isinstance(elements,int)):
            if((elements > 0) and (elements % 2 == 1)):
                count = count + 1
        else :
            print("ERROR! There is at least a non-int input.")
            return 0
    return count
                