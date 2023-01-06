import random
def play_game(p,c):
    if p==1 and c==2 or p==2 and c==1:
        result=2
    elif p==2 and c==3 or p==3 and c==2:
        result=3
    else:
        result=1
    if p==result:
        return 1
        userScore+=1
    else:
        return 0
        compScore+=1
def main():
    userScore=0
    compScore=0
    p=0
    print('Let\'s play Rock Paper Scissors!')
    while userScore<3:
        print('Your turn')
        print('Enter choice: ')
        print('1-Rock\t2-Paper\t3-Scissors')
        p=int(input())
        while p>3 or p<1:
            print('Enter Valid Input')
            p=int(input())
        print('You chose: ')
        if p==1:
            print('Rock')
        if p==2:
            print('Paper')
        if p==3:
            print('Scissors')
        print('\nComputer\'s Turn')
        c=random.randint(1,3)
        while p==c:
            c=random.randint(1,3)
        print('Computer Chose: ')
        if c==1:
            print("Rock")
        if c==2:
            print("Paper")
        if c==3:
            print("Scissor")
        win= play_game(p,c)
        if win==1:
            print('\nYou win!')
            userScore+=1
        else:
            print('\nComputer wins!')
            compScore+=1
    else:
            print('You won 3 times!')
            print('Computer\'s score= ',compScore)

    print('\nDo you want to play again?[y/n]')
    repeat=input()
    if repeat=='n' or repeat=='N':
        print('Thanks for playing!') 
    elif repeat=='y' or repeat=='Y':
        main()
    else:
        print('Please input a valid response')
        
        
main()


            
