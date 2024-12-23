def isbn_dictionary(filename):
    try :
        with open(filename, "r") as f:
            list = f.read().split('\n')
    except FileNotFoundError:
        print("The file {filename} was not found.")
        return None
    dict = {}
    for x in list:
        y = x.split(',')
        dict[y[2]] = (y[0], y[1])
    return dict
        
        
        
        
          
    


        