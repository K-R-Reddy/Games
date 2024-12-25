# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:25:09 2024

@author: dell
"""

def magic_square(n):
    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    print("The Sum of row/column/diagonal is "+str((n*(n**2+1))/2))
rc=int(input("Enter odd number : "))
magic_square(rc)
     