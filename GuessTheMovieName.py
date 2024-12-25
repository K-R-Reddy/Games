# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:33:27 2024

@author: dell
"""
import random
movies=['leo','spyder','bahubali','rebel','devara','pushpa','rrr','hanuman','robo','eega','saaho','kalki']
def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(" ")
        else:
            temp.append("*")
    qn=''.join(str(x) for x in temp)
    return qn
def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
    
def play():
    p1name=input("Enter Player1 Name : ")
    p2name=input("Enter Player2 Name : ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1name,"turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            '''print(picked_movie)

            for i in range(len(picked_movie)):
                print("_",end=" ")'''
            not_said=True
            while not_said:
                letter=input("\nGuess Letter : ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter : "))
                    if d==1:
                        ans=input("Guessed Movie Name : ")
                        if(ans==picked_movie):
                            pp1=pp1+1
                            print("Correct")
                            not_said=False
                            '''print(p1name,"! Your Score :",pp1)'''
                        else:
                            print("Wrong answer. Try Again.")
                else:
                    print(letter,'not found')
            c=int(input("Press 1 to continue or 0 to quit : "))
            if c==0:
                print(p1name,"Your Score : ",pp1)
                print(p2name,"Your Score : ",pp2)
                print("Thanks For Playing\nHave a Nice Day.")
                willing=False
        else:
            print(p2name,"turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            '''print(picked_movie)

            for i in range(len(picked_movie)):
                print("_",end=" ")'''
            not_said=True
            while not_said:
                letter=input("\nGuess Letter : ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie or 2 to unlock another letter : "))
                    if d==1:
                        ans=input("Guessed Movie Name : ")
                        if ans==picked_movie:
                            pp2=pp2+1
                            print("Correct")
                            not_said=False
                            '''print(p2name,"! Your Score :",pp2)'''
                        else:
                            print("Wrong answer. Try Again.")
                else:
                    print(letter,'not found')
            c=int(input("Press 1 to continue or 0 to quit : "))
            if c==0:
                print(p1name,"Your Score : ",pp1)
                print(p2name,"Your Score : ",pp2)
                print("Thanks For Playing\nHave a Nice Day.")
                willing=False
        turn=turn+1
play()