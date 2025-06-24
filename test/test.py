import random
from tkinter import *
from tkinter import font
import tkinter as tk
"""
def pasirinkimas():
    print("--------------------------------------------")
    g=input("[1] - Calculator, [2] - Game, [3] - Goodnight ")
    print("--------------------------------------------")
    if g=="1":
        calculator()
    elif g=="2":
        zaidimas()
    elif g=="3":
        print("Goodnight")
        exit() #choose the game

def calculator():
    while True:
        x=float(input("X = "))   
        y=float(input("Y = "))
        z=input("What operation you want to do? (+ - * /) ")
        if z == "+":
            result = x+y
        elif z == "-":
            result = x-y
        elif z == "*":
            result = x*y
        elif z == "/":
            result = x/y
        print(result)
        print("--------------------------------------------")
        again =input("Do you want to calculate more? ")
        if again.lower()!="yes":
            pasirinkimas() #calculator

def zaidimas():
    score=0
    while True:
        print("Little Game")
        print("--------------------------------------------")
        choices = ["scissors","paper", "rock"]
        psr=input("Pasirink: scissors, paper, rock ").lower()
        print("--------------------------------------------")
        kompas=random.choice(choices)
        if (psr == "scissors" and kompas == "scissors") or (psr == "paper" and kompas == "paper") or (psr == "rock" and kompas == "rock"):
            print("Computer chose: ",kompas.upper())
            print("You chose: ", psr.upper())
            print("--------------------------------------------")
            print("Draw!")
            print("--------------------------------------------")
        elif (psr == "scissors" and kompas == "paper") or (psr == "paper" and kompas == "rock") or (psr == "rock" and kompas == "scissors"):
            print("Computer chose: ",kompas.upper())
            print("You chose: ", psr.upper())
            print("--------------------------------------------")
            print("You won!")
            print("--------------------------------------------")
            score+=1
        elif (psr == "scissors" and kompas == "rock") or (psr == "paper" and kompas == "scissors") or (psr == "rock" and kompas == "paper"):
            print("Computer chose: ",kompas.upper())
            print("You chose: ", psr.upper())
            print("--------------------------------------------")
            print("You lost!, RETARD")
            print("--------------------------------------------")
            score-=1
        print("Your score: ",score)
        again =input("Do you want to play more? ")
        if again.lower()!="yes":
            pasirinkimas() #game

def labas():
    print("Welcome to the Gedvydas Kleberis Program")
    print("--------------------------------------------")
    name = input("What is your name? ")
    print("--------------------------------------------")
    print("Welcome,",name.upper(),"homeless mf") #intro message
"""
def modechange(): #change mode
    if moestas.config('image')[-1] == str(mode):
        moestas.config(image=modeevil)
    else:
        moestas.config(image=mode)
def show_game_selection(): #after submitting name show games
    zaidimasframe.pack_forget()
    resultsframe.pack_forget()
    gameselection.pack()
    gameframe.pack(anchor="center", pady=10)
    calculator = Button(gameframe, image=calc,
                       pady=20,
                       bg="#a3a3c2",
                       bd=10)
    gamerock = Button(gameframe, image=zirkles, command=game,
                      pady=20,
                      bg="#a3a3c2",
                      bd=10)
    calculator.pack(side=tk.LEFT, padx=10)
    gamerock.pack(side=tk.LEFT, padx=10)

def submitf(): #submit name
    name = vardas.get()
    if name:
        label1.config(text=f"Welcome, {name.upper()} homeless mf")
        welcome.pack_forget()
        vardas.pack_forget()
        submit.pack_forget()
        moestas.pack_forget()
        show_game_selection()

def game(): #rock paper scissors game
    gameselection.pack_forget()
    label1.pack_forget()
    gameframe.pack_forget()
    zaidimasframe.pack(side="bottom", pady=10)
    rockbtn=Button(zaidimasframe, image=rock,bd=10,bg="#a3a3c2")
    paperbtn=Button(zaidimasframe, image=paper,bd=10,bg="#a3a3c2")
    scissorsbtn=Button(zaidimasframe, image=scissors,bd=10,bg="#a3a3c2")

    choose=Label(window,
                    text="What will you choose?",
                    bg="#c2c2d6",
                    font=("Arial",18),
                    anchor="center",
                    padx=15,pady=15,
                    relief=RAISED)
    choose.pack()
    youchooseLabel=Label(youchooseframe,text="You chose: ",bg="#c2c2d6",font=("Arial",18,"bold")) #You chose text
    pcchooseLabel=Label(pcchooseframe,text="PC chose: ",bg="#c2c2d6",font=("Arial",18,"bold"))    #PC chose text

    youchoosePic=Label(youchooseframe,relief=RAISED,bd=10,bg="#a3a3c2")
    pcchoosePic=Label(pcchooseframe,relief=RAISED,bd=10,bg="#a3a3c2")

    youchooseframe.pack(side=tk.LEFT, pady=10)
    pcchooseframe.pack(side=tk.LEFT, pady=10)

    youchooseLabel.pack(anchor="center", padx=10)
    pcchooseLabel.pack(anchor="center", padx=10)
    youchoosePic.pack(side=tk.BOTTOM, padx=10)
    pcchoosePic.pack(side=tk.BOTTOM, padx=10)

    rockbtn.pack(side=tk.LEFT,padx=2)
    paperbtn.pack(side=tk.LEFT,padx=2)
    scissorsbtn.pack(side=tk.LEFT,padx=2)

    rockbtn.config(command=lambda: youchoose(rock))
    paperbtn.config(command=lambda: youchoose(paper))
    scissorsbtn.config(command=lambda: youchoose(scissors))
    choices = ["scissors","paper", "rock"]
    image_map = {"rock": rock, "paper": paper, "scissors": scissors}
    choice_name= ""
    choice= ""
    def youchoose(choice):
        youchoosePic.config(image=choice)
        youchoosePic.image = choice
        resultsframe.pack(side="top", pady=10)
        kompas=random.choice(choices)
        pcchoose(kompas)
        congrats(kompas,choice)
    def pcchoose(choice_name): #PC chooses randomly
        img = image_map[choice_name]
        pcchoosePic.config(image=img)
        pcchoosePic.image = img
    score=0
    def congrats(choice_name,choice):
        nonlocal score
        if (choice_name == "scissors" and choice == paper) or \
           (choice_name == "paper" and choice == rock) or \
           (choice_name == "rock" and choice == scissors):
            choose.config(text= "You lost!")
            score -= 1
        elif (choice_name == "scissors" and choice == rock) or \
             (choice_name == "paper" and choice == scissors) or \
             (choice_name == "rock" and choice == paper):
            choose.config(text= "You won!")
            score += 1
        else:
            choose.config(text= "Draw!")
    

window=Tk()
window.geometry("700x600")
window.title("Gedvydas Kleberis Program")
window.config(bg="#c2c2d6")

mode=PhotoImage(file="modeg.png")
modeevil=PhotoImage(file="modeevil.png")
calc=PhotoImage(file="calculator.png")
zirkles=PhotoImage(file="zirkles.png")
paper=PhotoImage(file="paper.png")
rock=PhotoImage(file="rock.png")
scissors=PhotoImage(file="scissors.png")

#welcome screen
label1 =Label(window,
             text="Welcome to the Gedvydas Kleberis Program",
             bg="#b3b3cc",
             font=("Arial",18,"bold"),
             pady=10,padx=10,
             borderwidth=10,
             relief=RAISED,
             )
welcome=Label(window,
              text="What is your name?",
              bg="#c2c2d6",
              font=("Arial",18))
moestas=Button(window,image=mode,
             pady=100,
             bg="black")
vardas=Entry(window,
             bg="#c2c2d6",
             font=("Arial",18),
             justify="center")
submit=Button(window,
              text="Submit",
              bg="#b3b3cc",
              font=("Arial",10),
              command=submitf,
              padx=5,pady=5,
              borderwidth=10,
              relief=RAISED)
moestas.config(command=modechange)
label1.pack()
welcome.pack(pady=20,padx=15,anchor="center")
vardas.pack(anchor="center",pady=5,padx=15)
submit.pack(pady=10,padx=15,anchor="center")
moestas.pack(pady=20,padx=15,anchor="w")
#welcome screen

#game selection
gameselection=Label(window,
                    text="What do you want to do?",
                    bg="#c2c2d6",
                    font=("Arial",18),
                    anchor="center",
                    pady=15)
gameframe = Frame(window, bg="#c2c2d6")
#game selection

#rock paper scissors game
zaidimasframe=Frame(window, bg="#c2c2d6")
resultsframe=Frame(window, bg="#c2c2d6")
youchooseframe=Frame(resultsframe, bg="#c2c2d6")
pcchooseframe=Frame(resultsframe, bg="#c2c2d6")
#rock paper scissors game
window.mainloop()

#labas()
#pasirinkimas()
