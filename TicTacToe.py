import tkinter as tk
from tkinter import *


#FUNCTII
def valori(theBoard):
    valori=[]
    a=[]
    n=0
    for j in list(theBoard.values()):
        a.append(j)
        n+=1
        if n==3:
            valori.append(a)
            n=0
            a=[]
    return valori

def afisare(theBoard):
    n=0
    for j in theBoard.values():
        print (j, end=" ")
        n+=1
        if n==3:
            print ()
            n=0

def verificare(valori):
    n=0
    
    #linie
    for i in range(3):
        if valori[i][0]=='x' and valori[i][1]=='x' and valori[i][2]=='x':
            label=Label(root,text="PLAYER 1 WINS!", relief=RAISED)
            label.grid()
            break
        elif valori[i][0]=='0' and valori[i][1]=='0' and valori[i][2]=='0':
            label=Label(root,text="PLAYER 2 WINS!", relief=RAISED)
            label.grid()
            break
        elif n==9:
            print ("remiza")
        else:
            n+=1
    #diagonale
    if valori[0][0]=='x' and valori[1][1]=='x' and valori[2][2]=='x' or valori[0][2]=='x' and valori[1][1]=='x' and valori[2][0]=='x':
            label=Label(root,text="PLAYER 1 WINS!", relief=RAISED)
            label.grid()
    elif valori[0][0]=='0' and valori[1][1]=='0' and valori[2][2]=='0' or valori[0][2]=='0' and valori[1][1]=='0' and valori[2][0]=='0':
            label=Label(root,text="PLAYER 2 WINS!", relief=RAISED)
            label.grid()
    else:
        n+=1
           
    #coloane
    for i in range(3):
        if valori[0][i]=='x' and valori[1][i]=='x' and valori[2][i]=='x':
            label=Label(root,text="PLAYER 1 WINS!", relief=RAISED)
            label.grid()
        if valori[0][i]=='0' and valori[1][i]=='0' and valori[2][i]=='0':
            label=Label(root,text="PLAYER 2 WINS!", relief=RAISED)
            label.grid()
        else:
            n+=1
    if n==0:
        label=Label(root,text="REMIZA!", relief=RAISED)
        label.grid()
            
    

root=tk.Tk()

label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=0, column=0)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=0, column=1)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=0, column=2)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=1, column=0)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=1, column=1)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=1, column=2)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=2, column=0)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=2, column=1)
label=Label(root, relief=RAISED, height=5, width=10)
label.grid(row=2, column=2)
#PROGRAM

theBoard={'top-L': [0,0],'top-M': [0,1],'top-R': [0,2],
          'mid-L': [1,0],'mid-M': [1,1],'mid-R': [1,2],
          'bot-L': [2,0],'bot-M': [2,1],'bot-R': [2,2]}




for i in range(4):
    print("Player 1 move: ", end='')
    player1=input().split()
    if player1[0] in list(theBoard.keys()):
        label=Label(root,text='X', relief=RAISED, height=5, width=10)
        label.grid(row=theBoard[player1[0]][0], column=theBoard[player1[0]][1])
        theBoard[player1[0]]=player1[1]
    else:
        print ('Pozitie incorecta, reintrodu:')
        player1=input().split()
        label=Label(root,text='X', relief=RAISED, height=5, width=10)
        label.grid(row=theBoard[player1[0]][0], column=theBoard[player1[0]][1])
        theBoard[player1[0]]=player1[1]
    verificare(valori(theBoard))
    print("Player 2 move: ", end='')
    player2=input().split()
    if player2[0] in list(theBoard.keys()):
        label=Label(root,text='0', relief=RAISED, height=5, width=10)
        label.grid(row=theBoard[player2[0]][0], column=theBoard[player2[0]][1])
        theBoard[player2[0]]=player2[1]
    else:
        print ('Pozitie incorecta, reintrodu:')
        player2=input().split()
        label=Label(root,text='0', relief=RAISED, height=5, width=10)
        label.grid(row=theBoard[player2[0]][0], column=theBoard[player2[0]][1])
        theBoard[player2[0]]=player2[1]
  
    verificare(valori(theBoard))

print("Player 1 move: ", end='')
player1=input().split()
theBoard[player1[0]]=player1[1]



verificare(valori(theBoard))