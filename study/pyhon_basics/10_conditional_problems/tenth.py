species = "dog"
age = 5

if species == "dog" and age < 2:
    print("Puppy food")
elif species == "dog" and age > 2:
    print("dog food")
elif species == "cat" and age < 5:
    print("junior cat food")
elif species == "cat" and age > 5:
    print("senior cat food")
else:
    print("Not mentioned species")