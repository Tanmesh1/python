# these are mutable types
my_list = [1, 2, 3] # list  
my_dict = {'a': 1, 'b': 2} # dictionary
my_set = {1, 2, 3} # set
# these are immutable types
my_int = 10 # integer
my_str = "hello" # string
my_tuple = (1, 2, 3) # tuple

def modify_list(lst):
    lst.append(4)
    return lst
def modify_string(s):
    s += " world"
    return s

print("Original list:", my_list)
modified_list = modify_list(my_list)

###  Inner working of immutable in python 
# In python , immutable types cannot be changed after they are created as value is created in memory location 
# it cannot be changed but a new value can be created and assigned to the same variable name as to variable it gives
# references to memory location of value as there is an garbage collector that will clean up the unreferenced memory locations
# IMMUTABLE TYPES: int, float, string, tuple, frozenset, bytes
# MUTABLE TYPES: list, dict, set, bytearray , Array
# ###