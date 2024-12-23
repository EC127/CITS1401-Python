n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.
p1 = 0
p2 = 1
sum = 2
if (n == 1) :
    print (0)

elif (n == 2) :
    print (1)

else :
    while (n != 3):
        p = p1 + p2
        p1 = p2
        p2 = p
        n = n-1
        sum = sum + p1 + p2
    print (sum)
        
        
        
        
        
    
    

    