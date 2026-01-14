# slicing in string     
# str[0:6] here last element is not included so gap is of 0 to 6
# 
# 
# 
# ###

# def leftrotate(lst,d):
#     return lst[d:] + lst[:d]
#     rot = []
#     for i in range(0,len(lst)):
#         rot.append(lst[i])
#     return rot
        

# lst = [10,20,30,40]
# d = 2
# rot = leftrotate(lst,d)
# print(rot)



#User function Template for python3

# class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    # def rotateArr(self, arr, d):
    #     n=len(arr)
    #     d=d%n
    #     if (n==0 or n==1):
    #         return
    #     a=0
    #     b=d-1
    #     while a<b:
    #         temp=arr[a]
    #         arr[a]=arr[b]
    #         arr[b]=temp
    #         a+=1
    #         b-=1
    #     a=d
    #     b=n-1
    #     while a<b:
    #         temp=arr[a]
    #         arr[a]=arr[b]
    #         arr[b]=temp
    #         a+=1
    #         b-=1
    #     a=0
    #     b=n-1
    #     while a<b:
    #         temp=arr[a]
    #         arr[a]=arr[b]
    #         arr[b]=temp
    #         a+=1
    #         b-=1
                


# a = [1998,2002]
# b = [2014,2016]

# print((a+b)*2)