master_pwd = input("What is master password? ")

def view():
    with open('password.txt','r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User:" , user, "Password:",passw)
    
def add():
    
    name = input("Please enter the name: ")
    pwd =  input("Please enter the password: ")
    
    with open('password.txt','a') as f:
        f.write(name+'|'+pwd+'\n')
    
while True:
    mode = input("Which mode would you like to activate view/add or would you like to quit by pressing q: ").lower()
    if mode == "q":
        print("You are out.")
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()    
    else:
        print("Invalid response")