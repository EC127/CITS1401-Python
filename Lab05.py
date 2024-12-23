def  sequence(n):
    list = []
    list.append(n)
    while n != 1 :
        if(n % 2 == 0):
            n=n//2
        else :
            n=n*3+1
        list.append(n)
    return list
print(sequence(12))

        

    

        
            
            
            
        
        
    
            
            

        
        

        

    
        

        

        
        
        
        
          
    


        