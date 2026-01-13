#start by getting gcd of number and after getting gcd divide array in those equal pieces 
# then we will juggle and override all first occuring element by their previous one
# and same for second occurence  and same for all occurence 
# ###


# Juggleing algo
# import math 

# def rotatearr(arr, d):
#     n = len(arr)
#     d %= n
#     cycle = math.gcd(n,d)
#     for i in range(cycle):
#         startele = arr[i]
#         curridx = i
#         while True:
#             nextidx = (curridx + d)%n 
#             if nextidx == i:
#                 break
#             arr[curridx] = arr[nextidx]
#             curridx = nextidx

#         arr[curridx] = startele


# reversal algorithm 
def rotateArr(arr,d):
    n = len(arr)
    d %= n
    reverse(arr, 0 ,d-1)
    reverse(arr , d ,n-1)
    reverse(arr,0,n-1)

def reverse(arr ,start , end):
    while start < end:
        arr[start], arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1