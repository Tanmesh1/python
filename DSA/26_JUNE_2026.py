def pal(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
s = "madm"
print(pal(s))


#fibo
def fibo(n):
    a,b = 0,1
    print(a)
    while(b<n):
        print(b)
        c = b+a
        a=b
        b=c

fibo(1000)

#fibo using recur
def fibo_r(n):
    if n<=1:
        return n
    else:
        return (fibo_r(n-1) + fibo_r(n-2))
    

n = 10
if n<=0:
    print("invalid")
else:
    for i in range(n):
        # print(i)
        print(fibo_r(i))

# compress
def compress(s):
    temp = len(s)
    new_s = ''
    count = 1
    for i in range(temp-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            new_s = new_s + s[i]+ str(count)
            count = 1
    new_s = new_s + s[n-1]+ str(count)
    return new_s


# fizzbuzz

def fizzbuzz(n):
    for i in range(1,n-1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(20)


# fizzbuzz with dict
def fizzbuzz2(n):
    d = {3:'fizz',
         5:'Buzz'}
    for i in range(1,n+1):
        result =""
        for k,v in d.items():
            if i%k==0:
                result+=v
        if not result:
            result = i
        print(result)

fizzbuzz(15)


# charachter occurence 
# least repeating charachter

def least_char_occurence(s):
    print(s)
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    result = min(ch,key= ch.get)
    print(result)


# prime number

def prime_num(n):
    flag = False
    if n > 1 :
        for i in range (2,n):
            if n%i == 0:
                flag = True
                break
        if flag:
            return "No! Its not a prime number"
        else:
            return "Yes! It is a prime number"
        

#using list 
def string_format(s):
    l = []
    temp = s.split('_')
    for i in temp:
        l.append(i[0].lower() + i[1:].upper())
    print(l)
    s =  '.'.join(l)
    print(s)   

# using String
def string_format1(s):
    new_s = ''
    temp = s.split('_')
    