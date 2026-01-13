def fact(n):
    fact1 = 1
    for i in range(1,n+1):
         fact1 = fact1 * i
         
    digit = 0
    while(fact1>0):
        digit = digit + 1
        fact1 = fact1//10
        
    return digit

n = fact(5)
print(n)