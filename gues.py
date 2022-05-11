import random
print("****WELCOME****")
name=input("enter your name")
print("***",name,"YOU ARE READY FOR THE GAME***")
print("***SO LETS START***")
number=[]
chances=0
def lumber():
    for i in range (5):
        a=random.randrange(0,9)
        number.append(a)
lumber()
print(number)
def game():
    global re
    re=[]
    ree=[]
    cow=0
    bull=0
    tries=0
    while tries<10:
        if tries==0:
            print("you have total 10 chances to win")
        if tries>0 and tries<=10:
            print("you have",10-tries,"chances left")
        use=int(input("please enter the number u want to guess:"))
        pos=int(input("please enter the position of that number:"))
        i=0
        while i<len(number):
            if use==number[i]:
                if pos==i:
                    bull=bull+1
                    re.append(use)
                    print(re)
            elif use==number[i]:
                if pos!=i:
                    ree.append(use)
                    print(ree)
                    cow=cow+1
            elif use not in number:
                cow=cow+1
            i=i+1
        if len(re)==len(number):
            print("you win")
            break
        tries=tries+1
                       
game()
if len(re)!=len(number):
            print("you loose")

    
def playagain():
    print("game over")
    user=input("if you want to play again write yes or no")
    if user=="yes":
        game()
    else:
        print(".....................")
playagain()