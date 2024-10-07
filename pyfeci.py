import tkinter as tk
import random
from tkinter import messagebox as tkMessageBox
from tkinter import *

nom = "user"
user_win = 0
userresult = "Vous avez gagné un point"
egalite = 0
computer_win = 0
computerresult = "L'ordinateur a gagné un point"
running = True

def click(choix):
    global user_win, egalite, computer_win
    ordi = random.randint(1, 3)

    if choix == "q":
        quitter = tkMessageBox.askyesno("Exit", "Êtes-vous sûr de vouloir quitter ?")
        if quitter:
            window.destroy()
        return

    if choix == "p":
        chx.config(text="Vous avez choisi Pierre")
    elif choix == "f":
        chx.config(text="Vous avez choisi Feuille")
    elif choix == "c":
        chx.config(text="Vous avez choisi Ciseau")
    else:
        chx.config(text="Mauvais choix")
        return

    # Déterminer le choix de l'ordinateur
    if ordi == 1:
        choixPC = "p"
        chxo.config(text="L'ordinateur a choisi Pierre")
    elif ordi == 2:
        choixPC = "f"
        chxo.config(text="L'ordinateur a choisi Feuille")
    else:
        choixPC = "c"
        chxo.config(text="L'ordinateur a choisi Ciseau")

    # Comparaison des choix
    if choix == choixPC:
        rslt.config(text="Partie nulle")
        egalite += 1
    elif (choix == "p" and choixPC == "f") or (choix == "f" and choixPC == "c") or (choix == "c" and choixPC == "p"):
        rslt.config(text=computerresult)
        computer_win += 1
    else:
        rslt.config(text=userresult)
        user_win += 1

    # Mise à jour du score
    score.config(text=f"{nom} : {user_win} / Égalités : {egalite} / Ordinateur : {computer_win}")

    # Vérification du gagnant
    if user_win == 3:
        tkMessageBox.showinfo("Vainqueur", "Vous avez gagné !")
        window.destroy()
    elif computer_win == 3:
        tkMessageBox.showinfo("Vainqueur", "L'ordinateur a gagné !")
        window.destroy()

# Création de la fenêtre principale
window = tk.Tk()
window.title("PyFeCi")
window.geometry("400x400")
window.minsize(400, 250)

# Image de fond
img = PhotoImage(file="font3.png")
lbl_bk = tk.Label(window, image=img)
lbl_bk.image = img
lbl_bk.place(relx=0.5, rely=0.5, anchor="center")

# Label de bienvenue
hello = tk.Label(window, text=f"Hello {nom}",
                 bg="#736357", fg="#C69C6D", font=("Arial", 20), width=20, height=2)
hello.pack()

# Question du choix
qustn = tk.Label(window, text=f"{nom}, Quel est votre choix : (p)ierre / (f)euille / (c)iseau ou (q)uitter :",
                 font=("Arial", 10), fg="#00FF00", bg="#006837")
qustn.pack(pady=(10, 10))

# Boutons pour les choix
pierre = tk.Button(window, text="Pierre", width=10, height=1, bg="#006837", fg="#00FF00", command=lambda: click("p"))
pierre.pack(pady=(0, 10))

feuille = tk.Button(window, text="Feuille", width=10, height=1, bg="#006837", fg="#00FF00", command=lambda: click("f"))
feuille.pack(pady=(0, 10))

ciseau = tk.Button(window, text="Ciseau", width=10, height=1, bg="#006837", fg="#00FF00", command=lambda: click("c"))
ciseau.pack(pady=(0, 10))

quitter_btn = tk.Button(window, text="Quitter", width=10, height=1, bg="#006837", fg="#00FF00", command=lambda: click("q"))
quitter_btn.pack(pady=(0, 10))

# Affichage des scores
score = tk.Label(window, text=f"{nom} : {user_win} / Égalités : {egalite} / Ordinateur : {computer_win}",
                 font=("Arial", 10), fg="#F15A24", bg="#999999")
score.pack()

# Affichage des choix
chx = tk.Label(window, text="", font=("Arial", 10), bg="#00FF00")
chx.pack()

chxo = tk.Label(window, text="", font=("Arial", 10), bg="#00FF00")
chxo.pack()

# Affichage du résultat
rslt = tk.Label(window, text="", font=("Arial", 10), bg="#00FF00")
rslt.pack()

window.mainloop()
