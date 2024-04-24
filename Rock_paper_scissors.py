import random 
print ('welcome to this rock,paper,scissors game ')
answer = input ('Do you wish to play (y/n)? ')

if answer.lower() == 'y':
    while True:
        choices = ['Rock', 'Paper', 'Scissors']
        val = random.randint(0,2)
        compChoice = choices[val]

        ans = input ('Which do you chose.. Rock,Paper,scissors or q to quit? ')
        if ans.lower() == 'q':
            print ('Thanks for playing')
            break
        elif ans.lower() not in ['rock','paper','scissors']:
            print ('Please enter a valid choice')
            continue
        else:
            if ans.lower() == compChoice.lower():
                print ("Computer chose" ,compChoice, "oops! you both made the same choices, Try Again")
                continue
            else:
                if ans.lower() == 'rock' and  compChoice == 'Scissors':
                    print("Computer chose" ,compChoice, "you win!")
                    continue
                elif ans.lower() == 'paper' and  compChoice == 'Rock':
                    print("Computer chose" ,compChoice,"you win!")
                    continue
                elif ans.lower() =='scissors' and  compChoice == 'Paper':
                    print("Computer chose" ,compChoice, "you win!")
                    continue
                else:
                    print("Computer chose" ,compChoice, "you lose!")
                    continue
                