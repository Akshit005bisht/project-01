import random
'''
1 for snake
-1 for water 
0 for gun

'''

computer = random.choice([-1,0,1])
youstr=input("enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}

you = youDict[youstr]

#by now we have two numbers computer and you

print(f"you choose {reverseDict[you]}\ncomputer choose{reverseDict[computer]}")

if (computer==you):
    print("its draw")
else:
    '''
    if(computer==-1 and you==1): (computer - you) = -2
        print("you win!")
    elif(computer==-1 and you==0):(computer - you) =  -1
        print("you loose!")
    elif(computer==1 and you==-1):(computer - you) =  2
        print("you loose!")
    elif(computer==1 and you==0):(computer - you) =  1
        print("you win!")
    elif(computer==0 and you==-1):(computer - you) =  1
        print("you win!")
    elif(computer==0 and you==1):(computer - you) =  -1
        print("you loose!")
        the below logic is written on the basis of the value of computer - you
        
        '''
        
    if((computer - you )== -1 or (computer - you)== 2):
        print("you loose")
    else:
        print("you win ")
    
