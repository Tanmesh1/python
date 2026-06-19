# pattern 1

for i in range(1,6):
    for j in range(1,6):
        print("*", end="")
    print()


# pattern 2

for i in range(1, 6):
    for j in range(1,i):
        print("*",end = "")
    print()

#pattern 3

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

print()
# pattern 4

for i in range(1,6):
    for j in range(1, i + 1):
        print(i, end = "")
    print()

print()
# pattern 5

for i in range(1,6):
    for j in range(i,6):
        print("*", end="")
    print()

print()
# pattern 6

for i in range(6,1,-1):
    for j in range(1,i):
        print(j, end="")
    print("")

# pattern 7

for i in range(1,5):
    for j in range(4,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

print()
# pattern 8

for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end = "")
    print()


print()
# pattern 9

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end = "")
    print()

print()

# pattern 10

for i in range (1,6):
    for j in range(i):
        print("*",end="")
    print()
for k in range(4,0,-1):
    for j in range(0,k):
        print("*", end="")
    print()

print()
# pattern 11
a = 1
for i in range(1,5):
    
    for j in range(i):
        if a==1:
            print("1",end="")
            a=0
        else:
            print("0", end = "")
            a=1
    print()

