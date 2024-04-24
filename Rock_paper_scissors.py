import random 
print ('welcome to this rock,paper,scissors game ')
answer = input ('Do you wish to play (y/n)? ')

if answer.lower() == 'y':
    while True:
        choices = ['Rock', 'Paper', 'Scissors']
        val = random.randint(2)
        compChoice = choices[val]

        ans = input ('Which do you chose.. Rock,Paper,scissors or q to quit? ')
        if ans.lower() == 'q':
            break
        else:
            if ans.lower() == compChoice.lower():
                print ("oops! you both made the same choices, Try Again")
                continue
            else:
                if ans.lower() == 'rock' and  compChoice == 'Scissors':
                    print("you win!")
                    continue
                elif ans.lower() == 'paper' and  compChoice == 'Rock':
                    print("you win!")
                    continue
                elif ans.lower() =='scissors' and  compChoice == 'Paper':
                    print("you win!")
                    continue
                else:
                    print("you lose!")
                    continue
                