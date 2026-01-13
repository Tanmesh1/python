def sortedlist(lst):
    if len(lst) == 0  or len(lst) == 1:
        return "yes"
    else:
        for i in range[1,len(lst)]:
            if lst[i-1] > lst[i]:
                return "No"
            else:
                return "Yes"
    


lst = [1,32,2,3,24]
print(sortedlist(lst))