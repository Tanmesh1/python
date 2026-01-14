password = "password"

if len(password) < 6 :
    print("weak")
elif len(password) < 10:
    print("Medium")
else:
    print("strong")