# binary search is searching algorithm in sorted array 
#  ###

def binary(arr,n):
    low = 0
    high = len(arr) 
    while(low <= high ):
        mid = (low + high)//2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            low = mid +1
        else:
            high = mid - 1  
    return -1

# first occurence using binary search
# def firstoccur(arr,n):
#     low = 0
#     high = len(arr)
#     first = 0
#     while(low <= high):
#         mid = (low + high)//2
#         if arr[mid] == n:
#             first = arr[mid]
#         elif arr[mid] < n:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return first 

arr = [1,2,3,4,4,5,6,7]
n = 4 
# print(firstoccur(arr,n))
print(binary(arr,n))
        
# print("hello World")


def count(arr,n):
    low = 0
    high = len(arr)
    count = 0 
    while(low <= high ):
        mid = (low + high)//2
        if arr[mid] == n:
            count += 1
            continue
            print(count)
           
        elif arr[mid] < n:
            low = mid +1
        else:
            high = mid - 1  
    return count


print(count(arr,n))

##binary search

def bina(arr,n,x):
    arr.sort()
    low = 0
    high = n-1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            high = mid - 1
        else:
            low = mid + 1
    return -1
