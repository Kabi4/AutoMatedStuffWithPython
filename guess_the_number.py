def rand_number():
    import random
    x=random.randint(1,10)
    return x

def play_game():
    print("I have guessed a number between 1 and 10")
    string=int(input("Can you guess my number?? Enter here: "))
    x=rand_number()
    ct=1
    while string!=x:
        print("Ooops!! it seems u didn't guess right.Try again :)")
        ct+=1            
        string=int(input())
    print("Hurray!! U guessed the right number in {} Try".format(ct))
    play_twice()    

def play_twice():
    play=str(input("Do you want to play again??Y/N: ")).lower()
    if play=='y':
        play_game()
    elif play=='n':
        print("Thankyou!! you for playing")
    else:
        print("Your output didn't match Y or N please try again!!!")
        play_twice()

def play_guess():
    s=str(input('Do you want to play guess the number?Y/N \n')).lower()
    if s=='y':
        play_game()
    elif s=='n':
        print("OK!! Have A Good Day")
    else:
        print("Your output didn't match Y or N please try again!!!")
        play_guess()


try:
    play_guess()
except EOFError:
    print("Your output didn't match Y or N please try again!!!")
    play_guess() 