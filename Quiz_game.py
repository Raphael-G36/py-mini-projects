print("Welcome to Who Wants To Be a Millionaire")

playing = input ("Do you want to play (Yes/No)? ")

if playing.lower() != "yes":
    quit()

print("Let's begin :)")

score = 0

Answer = input("how many generations of computers do we have? ")
if Answer == "5":
    print("That's Correct!")
    score+=1
else:
    print ("Incorrect!")


Answer = input("What does GPU stand for? ")
if Answer.lower() == "graphics processing unit":
    print("That's Correct!")
    score+=1

else:
    print ("Incorrect!") 

Answer = input("what Does CPU stand for? ")
if Answer.lower() == "central processing unit":
    print("That's Correct!")
    score+=1
else:
    print ("Incorrect!")

print ("congratulations, you Just completed the game!!")
print ("You answered " +str(int(score/3*100))+ "%" "correctly, and got "+str(int(100-(score/3)*100))+"% wrong.")


