import random

def labas():
    print("Welcome to the Gedvydas Kleberis Calculator")
    print("--------------------------------------------")
    name = input("Koks tavo vardas? ")
    print("--------------------------------------------")
    print("Sveikas atvykes,",name.upper(),"bedarbi tu")
    print("--------------------------------------------")
labas()

def calculator():
    while True:
        x=float(input("X = "))   
        y=float(input("Y = "))
        z=input("Kokia operacija nori atlikti? (+ - * /) ")
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
        again =input("Nori skaiciuoti daugiau? ")
        if again.lower()!="taip":
            break
calculator()

def zaidimas():
    score=0
    while True:
        print("Zaidimukas")
        print("--------------------------------------------")
        choices = ["zirkles","popierius", "akmuo"]
        psr=input("Pasirink: zirkles, popierius, akmuo ").lower()
        print("--------------------------------------------")
        kompas=random.choice(choices)
        if (psr == "zirkles" and kompas == "zirkles") or (psr == "popierius" and kompas == "popierius") or (psr == "akmuo" and kompas == "akmuo"):
            print("Kompiuteris pasirinko: ",kompas.upper())
            print("Tu pasirinkai: ", psr.upper())
            print("--------------------------------------------")
            print("Lygiosios")
            print("--------------------------------------------")
        elif (psr == "zirkles" and kompas == "popierius") or (psr == "popierius" and kompas == "akmuo") or (psr == "akmuo" and kompas == "zirkles"):
            print("Kompiuteris pasirinko: ",kompas.upper())
            print("Tu pasirinkai: ", psr.upper())
            print("--------------------------------------------")
            print("Laimejai!")
            print("--------------------------------------------")
            score+=1
        elif (psr == "zirkles" and kompas == "akmuo") or (psr == "popierius" and kompas == "zirkles") or (psr == "akmuo" and kompas == "popierius"):
            print("Kompiuteris pasirinko: ",kompas.upper())
            print("Tu pasirinkai: ", psr.upper())
            print("--------------------------------------------")
            print("Pralaimejai!, GAIDYS")
            print("--------------------------------------------")
            score-=1
        print("Tavo taskai: ",score)
        again =input("Nori zaisti daugiau? ")
        if again.lower()!="taip":
            break
zaidimas()