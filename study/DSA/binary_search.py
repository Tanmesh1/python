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

# arr = [1,2,3,4,4,5,6,7]
# n = 4 
# # print(firstoccur(arr,n))
# print(binary(arr,n))
        
# # print("hello World")


# def count(arr,n):
#     low = 0
#     high = len(arr)
#     count = 0 
#     while(low <= high ):
#         mid = (low + high)//2
#         if arr[mid] == n:
#             count += 1
#             continue
#             print(count)
           
#         elif arr[mid] < n:
#             low = mid +1
#         else:
#             high = mid - 1  
#     return count


# print(count(arr,n))


# Index of first occurence 


# we need to create an program that helps us to get first occurence of an x in sorted array using binary search 


def firstapper(arr,x):
    n = len(arr)
    first = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            first = mid
            high = mid - 1

        elif arr[mid] < x:
            low = mid +1   
        else:
            high = mid - 1

           
            
    return first


# arr = [1,2,3,3,3,5,6,7]
# x = 3
# print(firstapper(arr,x))



# last appearence

def lastappear(arr , x):
    low = 0 
    high = len(arr) - 1
    last = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] <  x:
            low = mid + 1
        else:
            high = mid - 1

    return last

arr = [1,2,3,3,3,5,6,7]
x = 3
print(lastappear(arr,x))
