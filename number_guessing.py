import random as rand

number= rand.randint(1,100)
print ("I have selected a random number from 1 to 100, you have three attempts to guess the number")
hey = input("first attempt : ")
if hey.isdigit():
    answer = int(hey)
else :
    print ("please enter a number")
    quit()  
while answer != number:
    if answer > number:
            print ("Too high")
            answer = int(input("next attempt : "))
    else:
            print ("Too low")
            answer = int(input("next attempt : "))

print ("you found it!!")
print ("The number was : ", number)
quit()
