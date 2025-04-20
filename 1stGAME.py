import random

computer = random.choice([1,-1,0])
youstr=(input("enter your choice:"))
youDict= {"s" :1,"p":-1,"sc":0}
reverseDict = {1:"stone",-1:"paper",0:"scissor"}
you = youDict[youstr]
print(f"you chose: {reverseDict[you] }\n computer chose :{reverseDict[computer]}")

if(computer==you):
    print("its a draw")
else:
    if(computer== -1 and you==1):
        print("you lose!!")
    if(computer== -1 and you==0):
        print("you win!!")
    if(computer== 1 and you==-1):
        print("you win!!")
    if(computer== 1 and you==0):
        print("you lose!!")
    if(computer== 0 and you==1):
        print("you win!!")
    if(computer== 0 and you==-1):
        print("you lose!!")
    
    else:
        print("something went wrong")
