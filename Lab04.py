def list_sorting(lst1,lst2):
    zipped=zip(lst2,lst1)
    sorted_pairs = sorted(zipped, key= lambda x: (-x[0], x[1]))   
    result = zip(*sorted_pairs)
    names, ages = [list(x) for x in result]
    return names, ages

    
        




    
