# pattern 12

for i in range(1,5):
    j=1
    while(j<=i):
        print(j,end="")
        j=j+1
    for k in range(4,i,-1):
        print("*", end="")
    for l in range(i,0,-1):
        print(l, end="")
    print()







