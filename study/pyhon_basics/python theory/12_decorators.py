## Question 1

# import time 

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result  = func(*args ,**kwargs)
#         end = time.time()
#         print(f"{func.__name__} run in {end-start} time")
#         return result
#     return wrapper


# @timer
# def example_function(n):
#     time.sleep(n)


# example_function(2)


#Question 2

def debug(func):
    def wrapper(*args , **kwargs):
        args_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{k}={v}"for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_values} and kwargs {kwargs_values}")
        return func(*args,**kwargs)
    return wrapper

@debug
def greet(name,greeting = "Hello "):
    print(f"{greeting}, {name}")

greet("chai", greeting = "hanji ")



# #User function Template for python3

# def nCr(n,r):
#     if r==0 or r==n:
#         return 1
    
#     return nCr(n-1,r-1) + nCr(n-1,r)
    



