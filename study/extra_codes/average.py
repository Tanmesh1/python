def average(my_list):
    avg = 0
    total = 0
    for i in range(0,len(my_list)):
        total = total + my_list[i]
    return total/len(my_list)
    
    
my_list = [1,1,2,3,1]
print(average(my_list))