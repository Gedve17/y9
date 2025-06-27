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
    calculatorBtn.pack(side=tk.LEFT, padx=10)
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
    zaidimasframe.pack_forget()
    zaidimasframe.pack(side="bottom", pady=10)
    
    
    score=0
    
    
    topframe.pack(side="top", pady=10,fill="x")
    

    topframe.columnconfigure(0, weight=1)
    topframe.columnconfigure(1, weight=3)
    topframe.columnconfigure(2, weight=1)

    back.grid(row=0, column=0, sticky="w", padx=18) #Back button to return to game selection
    choose.grid(row=0, column=1, sticky="nsew")
    taskai.grid(row=0, column=2, sticky="e", padx=10)

   

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

    def congrats(choice_name,choice):
        nonlocal score
        if (choice_name == "scissors" and choice == paper) or \
           (choice_name == "paper" and choice == rock) or \
           (choice_name == "rock" and choice == scissors):
            choose.config(text= "You lost!")
            score -= 1
            taskai.config(text=f"Your score: {score}")
        elif (choice_name == "scissors" and choice == rock) or \
             (choice_name == "paper" and choice == scissors) or \
             (choice_name == "rock" and choice == paper):
            choose.config(text= "You won!")
            score += 1
            taskai.config(text=f"Your score: {score}")
        else:
            choose.config(text= "Draw!")
    
def calculator():
    gameselection.pack_forget()
    label1.pack_forget()
    gameframe.pack_forget()
    zaidimasframe.pack_forget()
    backcalc.pack(anchor="w")
    fullframecalc.pack(side="bottom", pady=10)
    answercalc.pack(side="top", pady=10, padx=10, fill="x")
    buttonsframe.pack(side="bottom", pady=10)
    calc7.grid(row=0, column=0)
    calc8.grid(row=0, column=1)
    calc9.grid(row=0, column=2)
    calcdiv.grid(row=0, column=3)
    clearbtn.grid(row=0, column=4, sticky="nsew") #Clear button to reset the calculator
    calc4.grid(row=1, column=0)
    calc5.grid(row=1, column=1)
    calc6.grid(row=1, column=2)
    calcmult.grid(row=1, column=3)
    calculate.grid(row=1,rowspan=3, column=4,)
    calc1.grid(row=2, column=0)
    calc2.grid(row=2, column=1)
    calc3.grid(row=2, column=2)
    calcplus.grid(row=2, column=3)
    calcroot.grid(row=3, column=0)
    calc0.grid(row=3, column=1)
    calcdot.grid(row=3, column=2)
    calcminus.grid(row=3, column=3)

window=Tk()
window.geometry("1000x600")
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
calculatorBtn = Button(gameframe, image=calc, command=calculator,
                       pady=20,
                       bg="#a3a3c2",
                       bd=10)
gamerock = Button(gameframe, image=zirkles, command=game,
                      pady=20,
                      bg="#a3a3c2",
                      bd=10)
#game selection

#rock paper scissors game
zaidimasframe=Frame(window, bg="#c2c2d6")
resultsframe=Frame(window, bg="#c2c2d6")
youchooseframe=Frame(resultsframe, bg="#c2c2d6")
pcchooseframe=Frame(resultsframe, bg="#c2c2d6")
topframe=Frame(window, bg="#c2c2d6")
rockbtn=Button(zaidimasframe, image=rock,bd=10,bg="#a3a3c2")
paperbtn=Button(zaidimasframe, image=paper,bd=10,bg="#a3a3c2")
scissorsbtn=Button(zaidimasframe, image=scissors,bd=10,bg="#a3a3c2")
taskai=Label(topframe,bg="#a3a3c2",font=("Arial",18,"bold"),bd=10,relief=RAISED)
back=Button(topframe, text="Back",
                bg="#a3a3c2",
                font=("Arial", 18),borderwidth=10,relief=RAISED,
                command=lambda: (topframe.pack_forget(), zaidimasframe.pack_forget(), resultsframe.pack_forget(),label1.pack(),buttonsframe.pack_forget(), gameselection.pack(), gameframe.pack(anchor="center", pady=10)))
choose=Label(topframe,
                    text="What will you choose?",
                    bg="#a3a3c2",
                    font=("Arial",18),
                    anchor="center",
                    padx=15,pady=15,bd=10,
                    relief=RAISED)
youchooseLabel=Label(youchooseframe,text="You chose: ",bg="#c2c2d6",font=("Arial",18,"bold")) #You chose text
pcchooseLabel=Label(pcchooseframe,text="PC chose: ",bg="#c2c2d6",font=("Arial",18,"bold"))    #PC chose text
youchoosePic=Label(youchooseframe,relief=RAISED,bd=10,bg="#a3a3c2")
pcchoosePic=Label(pcchooseframe,relief=RAISED,bd=10,bg="#a3a3c2")
#rock paper scissors game

#calculator
fullframecalc=Label(window, bg="#c2c2d6", font=("Arial", 18, "bold"), pady=20, padx=10, bd=10, relief=RAISED)
answercalc=Label(fullframecalc, text=" ", bg="#a3a3c2", font=("Arial", 18), pady=10, padx=10, bd=10, relief=RAISED) #label for result
buttonsframe=Frame(fullframecalc, bg="#c2c2d6")
clearbtn= Button(buttonsframe, text="C", bd=10, bg="#a3a3c2", font=("Arial", 18, "bold"), command=lambda: answercalc.config(text=" ")) #Clear button
calculate=Button(buttonsframe, text="=", bd=10, bg="#a3a3c2", font=("Arial", 18, "bold"), command=lambda: answercalc.config(text=str(eval(answercalc.cget("text"))))) #Calculate button
calc7 = tk.Button(buttonsframe, text="7",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "7"))
calc8 = tk.Button(buttonsframe, text="8",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "8"))
calc9 = tk.Button(buttonsframe, text="9",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "9"))
calcdiv = tk.Button(buttonsframe, text="/ ",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "/"))

calc4 = tk.Button(buttonsframe, text="4",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "4"))
calc5 = tk.Button(buttonsframe, text="5",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "5"))
calc6 = tk.Button(buttonsframe, text="6",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "6"))
calcmult = tk.Button(buttonsframe, text="* ",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "*"))

calc1 = tk.Button(buttonsframe, text="1",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "1"))
calc2 = tk.Button(buttonsframe, text="2",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "2"))
calc3 = tk.Button(buttonsframe, text="3",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "3"))
calcplus = tk.Button(buttonsframe, text="+",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "+"))

calcroot = tk.Button(buttonsframe, text="\u221A",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "\u221A")) #Square root button
calc0 = tk.Button(buttonsframe, text="0",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "0"))
calcdot = tk.Button(buttonsframe, text=". ",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "."))
calcminus = tk.Button(buttonsframe, text="- ",bd=10,bg="#a3a3c2",font=("Arial",18,"bold"), command=lambda: answercalc.config(text=answercalc.cget("text") + "-"))
backcalc=Button(window, text="Back",
                bg="#a3a3c2",
                font=("Arial", 18),borderwidth=10,relief=RAISED,
                command=lambda: (label1.pack(),buttonsframe.pack_forget(), gameselection.pack(), gameframe.pack(anchor="center", pady=10),backcalc.pack_forget(),fullframecalc.pack_forget()))
#calculator

window.mainloop()
