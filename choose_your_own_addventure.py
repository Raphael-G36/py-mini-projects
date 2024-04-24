print("welcome to the game!")
val = input("Do you want to undergo this adventure?(yes/no)")
if val.lower() == "yes":
    print("Great! Let's begin!")
    Q1=input ("You are on a dirt bike, heading down a hill. oops! You reached a dead end. Do you wish to turn left or right?")
    if Q1 == "left":
        print ("you turned left and OOps! You rode across a cliff and were severed brutally by an incoming helicopter blade...")
        quit()
    elif Q1 == "right":
       Q2 = input("you turned right and you came across an large farm with an old looking house at its center. Doy you wish to approach the farm or not? (Approach/ignore)")
       if Q2.lower() == "approach":
            Q3 = input("you approach the house and you see a girl sitting on a chair. Do you wish to approach her or not? (Approach/ignore)")
            if Q3.lower() == "approach":
                Q4 = input("you approach the girl and she asks you if you want to play a game. Do you wish to play a game or not? (Play/ignore)")
                if Q4.lower() == "play":
                    print("you play the game and you win!")
                    quit()
                elif Q4.lower() == "ignore":
                    print("you ignore the girl and you go back to your bike.")
                    quit()
            elif Q3.lower() == "ignore":
                print("you ignore the girl and you go back to your bike.")
                quit()
else:
    print("Okay, see you next time!")
    quit()

