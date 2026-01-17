# Algorithm based on recusion
# .Dynamic Programming
# .Backtracking
# .Divide and Conquer (binary search , quick sort and merge sort)
# 
# ###

#Decimal to binary conversion code using recursion

# def bina(n):
#     if n == 0:
#         return
#     bina(n//2)
#     print(n%2)


# def fun(n):
#     if n==0:
#         return
#     print("gfg")
#     fun(n-1)
    
# print(fun(5))
   


# def nto1(n):
#     if n==0:
#         return
#     print(n)
#     nto1(n-1)

# nto1(5)

# Tail recurssion : A recursive function is called tail recurcive if the function does not do anything  after the last recursive call.
# 
# base case 
# def facto(n):
#     if n==0:
#         return 1
#     return n*facto(n-1)


# print(facto(5))
     
def dSum(n): 
    if n < 10: 
        return n 
    return dSum(n // 10) + n % 10 
print(dSum(253))

