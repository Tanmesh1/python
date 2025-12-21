from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is master password? ")
key = load_key() +  master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
'''


def view():
    with open('password.txt','r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User:" , user, "| Password:", fer.decrypt(passw.encode()))
    
def add():
    
    name = input("Please enter the name: ")
    pwd =  input("Please enter the password: ")
    
    with open('password.txt','a') as f:
        f.write(name+'|'+ fer.encrypt(pwd.encode()).decode()+'\n')
    
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