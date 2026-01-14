# Internal working of python
# There are reference count for memory management in python
# ti get there reference count we can use sys module
# import sys and use sys.getrefcount(object)
# but it give almost same number every time as there is no way to determine the exact reference count due to optimizations
# note - Data type is assigned to the object not to the variable so we do not declare data type of variable in python
# garbage collector in python is used to clean up the unreferenced memory locations but it is not immediate it runs periodically to clean up the memory
# is operator is used to check the memory location of the object or reference of the object.
# ###