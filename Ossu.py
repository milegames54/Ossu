print("Zdravo ne srecnice upravo si ga popusio verovatno sad mislis sta sam sad uradio ali nista ti nece pomoci.")

Pitanje1 = input("Citaj ovo veoma pazljivo?")
if Pitanje1 == "Ok":
    print("Dobro.")
    
print("Verovatno sad zelis da iskljucis ovaj virus ili nesto slicno ali strpi se bices ovde dugo.")
print("Citaj ovo sad pazljivo, imas da mi platis 300 dinara za pepsu i pivo i da mi das tvoje licne podatke ili cu ti izbrisati sve podatke sa kompjutera, imas 6 sati.")
Pitanje1 = input("Budi spreman zato sto ako ugasis ovaj virus bice jos vise virusa ako na sva ova pitanja odgovoris tacno bice sve u redu ako si procitao napisi Ok?")
if Pitanje1 == "Luka":
    print("Ok.")
    points += 1
print("Posto sam te zajebao citajuci ovo veoma pazljivo nisi ni provalio da ti se kompjuter polako gasi i brise sve tvoje podatke, 300 dinara ces mi ostaviti ispod stepenica u skoli zivadin apostolovic.")
ime = input("Pre nego sto pocnemo zelim ti reci da budes 100% iskren napisi Ok ako se slazes ako na nesto slazes bices punisovan?")
points = 0
print("imas 24 sata da mi otkrijes sve tvoje podatke.")
print("Ja ves znam tvoje podatke, hakovao sam ti kameru i video sve, cak i tvoj tukic 0.1mm.")
print("Ukoliko pokusas da me prevaris ceo svet ce znati velicinu tvoj tukica na deep webu.")

Pitanje1 = input("Kako se zoves?")
if Pitanje1 == "Luka":
    print("Dobro.")
    points += 1

else:
    print("Nisi lepo odgovorio, ako to uradis jos jednom svi ce znati tvoju adresu.")
    points -= 1

Pitanje2 = input("Koliko imas godina?")
if Pitanje2 == "13":
    print("Dobro.")
    points += 1

else:
    print("Nisi lepo odgovorio, ok svi znaju tvoju adresu.")
    points -= 1
Pitanje3 = input("Kako ti se zove devojka?")
if Pitanje1 == "Natasa":
    print("HA HA hvala na svemu vec sam znao a sada pogledaj svoj pc.")
    points += 1

else:
    print("Reci zbogom svojoj graficki zato sto ce da se preprzi :)")
    points -= 1

import random
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 60)))
        win.overrideredirect(1)
        Label(win, text="Thank you for your IP adress", fg="Black").place(relx=.38, rely=.3)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.05)


threading.Thread(target=placewindows).start()

root.mainloop()

clear

print("Error")
