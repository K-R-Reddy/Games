# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:51:33 2024

@author: dell
"""
#Three Doors Wins
import random
doors=[0]*3
goatdoor=[0]*2
won=0
swap=0#no of swap wins
dont_swap=0#no of dont swap wins
j=0
while(j<10):
    
    x=random.randint(0,2)
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
        goatdoor.append(i)
    choice=int(input("Enter your choice : "))
    door_open=random.choice(goatdoor)
    while(door_open==choice):
        door_open=random.choice(goatdoor)
    ch=input("Do you want to swap? y/n : ")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("Player Wins")
            won=won+1
        else:
            print("Player Lost")
            dont_swap=dont_swap+1
    else:
        if(doors[choice]=='Goat'):
            print("Player Lost")
            swap=swap+1
        else:
            print("Player Wins")
            won=won+1
    j=j+1
print("Player Wons :",won,"times")
print("swap : ",swap)
print("Don't Swap :",dont_swap)