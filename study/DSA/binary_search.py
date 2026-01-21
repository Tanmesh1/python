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