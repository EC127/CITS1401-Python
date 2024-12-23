def binarytodecimal(binary):
    b = list(binary)
    total = 0
    i = 0
    while i < len(b):
        if b[i] == '1':
            total = total + pow(2,len(b)-1-i)
        i = i+1
    return total

print(binarytodecimal('011100100'))

        

        
        
    

