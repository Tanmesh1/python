# Linked list is used for non-continous memory allocation
# node =  info + next location address
# it is mostly used for runtime memory allocation
# need to create an reference variable for starting node 
# last block will store none in location address
# constructor is used to create another block
# two pointers are created for using singly linked list head and temp and head stays at the same memory location
# memory allocation is done by __init__
# self is used for storing the memory location of object that init function is going to make 
# 
# ###

class Node:
     def __init__(self,info,next):
          pass