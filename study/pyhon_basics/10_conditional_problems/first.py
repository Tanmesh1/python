def grupcat(age):
    if age<13:
        return "Child"
    elif age >= 13 and age <= 19:
        return "teenager"
    elif age >= 20 and age <= 59:
        return "Adult"
    else:
        return "Senior"
    
a = int(input("Give me an number: "))
print(grupcat(a))   