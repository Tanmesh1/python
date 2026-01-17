# python see's all loops in iteration tools 
# iterable objects (lists, file)
# response (__next__)
# step 1 : Iteration tool sends iter method to iterable object then after that iterable object send (__next__) as an reponse
# iterable object only refers to the starting point of the list then send the response(__next__) which tell that there are more values
# Then iter tool start using next() method for iterating
# when it reaches to final value it raises exception(stop iteration exception) that stops the loop 
# To open the file in current folder we just need to run open() method in   CLI AND readline() method helps to read all the lines in the files 
# file has it's own iter tool.
# we can define iter which is method and we can provide any iterable object 
# 
# 
# 
# ###

test = "" 
if not test:  #if not only finds if variable is empty or not
    print("Test does not have any value")


mylist = [1,2,3,4]
I = iter(mylist) #holds the reference of iter
#list iterator always points at starting value there is an internal pointer for iterating

#File is actual iteratable object but list is not an iteratable object it containes reference of the value