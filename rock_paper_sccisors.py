import random

def play_twice():
    play=str(input("Do you want to play again??Y/N: ")).lower()
    if play=='y':
        game()
    elif play=='n':
        print("Thankyou!! you for playing")
    else:
        print("Your output didn't match Y or N please try again!!!")
        play_twice()


def computer_guess():
    l=['Rock','Paper','Scissors']
    x=random.shuffle(l)
    return l[0]

def game():
    n=int(input("Enter the wining score: "))
    w,l,t=0,0,0
    print("Starting game......")
    while w<n and l<n:
        print("Win {} Loss {} Tie {}".format(w,l,t))
        com=computer_guess()
        x=int(input('Enter your choice (1)Rock (2)Paper (3)Scissors : '))
        ln=['Rock','Paper','Scissors']
        if x==1 or x==2 or x==3:    
            player=ln[x-1]
            print(player+" Verses.....")
            print(com)
            if com==player:
                t+=1
            else:
                if player=='Rock' and com=='Scissors':
                    w+=1
                elif com=='Rock' and player=='Scissors':
                    l+=1
                elif player=='Paper' and com=='Scissors':
                    l+=1
                elif com=='Paper' and player=='Scissors':
                    w+=1     
                elif com=='Rock' and player=='Paper':
                    w+=1
                elif player=='Rock' and com=='Paper':
                    l+=1
        else:
            print("Your enterted a unwanted value!!! Restarting The game......")
            game()
            
    if w==n:
        print("Hurray you win!!")
    else:
        print("You lose Better luck next time!! :-) ")
    play_twice()
    
def main():
    print("Welcome to the Rock,Paper,Scissors")
    game()
main()

    