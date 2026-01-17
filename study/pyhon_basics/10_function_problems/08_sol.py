def print_kwarg(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwarg(name = "shaktiman")
print_kwarg(name = "shaktiman" , powers = "superstrength" , enemy = "")
print_kwarg(name = "shaktiman" , powers = "superstrength")