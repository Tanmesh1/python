# sum of even numbers

n = 56
sum = 0
for i in range(0,n+1):
    if i%2 == 0:
        sum = sum + i
        print(i)
    else:
        continue
print(sum)    