import random
from tkinter import *
from tkinter import font
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

def modechange():
    if moestas.config('image')[-1] == str(mode):
        moestas.config(image=modeevil)
    else:
        moestas.config(image=mode)
def submitf():
    name = vardas.get()
    if name:
        label1.config(text=f"Welcome, {name.upper()} homeless mf")
        welcome.pack_forget()
        vardas.pack_forget()
        submit.pack_forget()
        moestas.pack_forget()

window=Tk()
window.geometry("600x600")
window.title("Gedvydas Kleberis Program")
window.config(bg="#c2c2d6")

mode=PhotoImage(file="modeg.png")
modeevil=PhotoImage(file="modeevil.png")
calc=PhotoImage(file="calculator.png")

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
calculator=Button(window,image=calc,
                  anchor="center",
                  pady=20)


gamerock=Button(window,)

gameselection.pack()
calculator.pack()
gamerock.pack()

window.mainloop()

#labas()
#pasirinkimas()
