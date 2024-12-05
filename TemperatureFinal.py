

import tkinter as tk

# Fonction de conversion de Fahrenheit en Celsius
def Convertir():
    try:
        # Récupérer la valeur de Fahrenheit entrée
        fahrenheit = float(entry_fahrenheit.get())
        # Calculer la conversion en Celsius
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        # Afficher la température en Celsius dans la label
        label_resultat.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        # Si l'entrée n'est pas un nombre valide
        label_resultat.config(text="Veuillez entrer un nombre valide.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.geometry("300x200")
fenetre.title("Convertisseur Fahrenheit en Celsius")

# Création des éléments de l'interface
label_instruction = tk.Label(fenetre, text="Entrez la température en Fahrenheit:")
label_instruction.pack(padx=10, pady=10)

entry_fahrenheit = tk.Entry(fenetre)
entry_fahrenheit.pack(padx=10, pady=10)

button_convertir = tk.Button(fenetre, text="Convertir", command=Convertir)
button_convertir.pack(pady=10)

label_resultat = tk.Label(fenetre, text="La conversion apparaîtra ici.", font=('Helvetica', 12))
label_resultat.pack(pady=10)

# Démarrer l'interface graphique
fenetre.mainloop()
