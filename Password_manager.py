from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#         print("Key generated and saved to key.key")

# write_key()

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)



def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
           led = line.rstrip()
           name, password = led.split("|")
           print('Account Name =', name, ', Password =',fer.decrypt(password.encode()).decode()) 

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() +"\n")


while True:
    mode = input("Would you like to add a new password or view an existing ones (view/add) or type q to quit?")
    if mode.lower() == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print ("Enter a valid input")
        continue