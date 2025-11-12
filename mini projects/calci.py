def cal(x , y , z ):
    if x == '+':
        return y + z
    elif x == "-":
        return y - z
    elif x == "*":
        return y * z
    elif x == "/":
        return y/z
    else:
        return "Invalid Operation"

x = input("Enter the operation you want to perform :")
y = int(input("Enter first number :"))  
z = int(input("Enter Secont number :"))
print(cal(x,y,z))