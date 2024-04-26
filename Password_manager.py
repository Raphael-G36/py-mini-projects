Master_pwd = input("Enter master password: ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
           led = line.rstrip()
           name, password = led.split("|")
           print('Account Name =', name, ', Password =', password)

def add():
    name = input("Enter Account name: ")
    pwd = input("Enter password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd +"\n")


def delete():
    pass

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