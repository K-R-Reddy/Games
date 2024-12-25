# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:31:07 2024

@author: dell
"""

#ROCK PAPER SCISSOR GAME
def r_p_s(ps1,ps2,pp1,pp2):
    pp1=pp1%3
    pp2=pp2%3  
    if(po[pp1]==pt[pp2]):
        print("Draw")
    elif((po[pp1]=='Rock'and pt[pp2]=='Scissor') or (po[pp1]=='Scissor' and pt[pp2]=='Paper') or (po[pp1]=='Paper' and pt[pp2]=='Rock') ):
        print(p1,"Wins")
        ps1=ps1+1
    else:
        print(p2,"Wins")
        ps2=ps2+1
    return ps1,ps2
po={0:'Rock',1:'Paper',2:'Scissor'}
pt={0:'Scissor',1:'Paper',2:'Rock'}
ps1=0
ps2=0
p1=input("Player One! Enter your Name : ")
p2=input("Player two! Enter your Name : ")
while(1):
    print(p1,"Enter your choice : ")
    num1=int(input())
    print(p2,"Enter your choice : ")
    num2=int(input())
    ps1,ps2=r_p_s(ps1,ps2,num1,num2)
    ch=input("Do you want to continue ? y/n : ")
    if(ch=='n'):
        break
print(p1,"score is",ps1)
print(p2,"score is",ps2)
if(ps1>ps2):
    print(p1,"Wins the Game😁")
    print(p2,"Better Luck Next Time!!😢")
else:
    print(p2,"Wins the Game😁")
    print(p1,"Better Luck Next Time!!😢")
    
    
    