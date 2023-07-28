from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


m_pwd = input("Enter the master password\n")
key=load_key() + m_pwd.encode()
fer=Fernet(key)

def view():
    with open('Password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user,"| Password:",fer.decrypt(passw.encode()).decode())



def add():
    name=input("Account Name:")
    pwd=input('Password:')

    with open('Password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

     


while True:
    mode = int(input("Would you like to(select option)  \n 1:view password \n 2:add password \n 3:quit \n"))
    print()
    if mode==3:
        break
    if mode==1:
        view()
    elif mode==2:
        add()
    else :
        print("Invalid code")
        continue
    print()
