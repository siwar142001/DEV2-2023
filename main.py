from libs.parking import Parking 
from libs.emplacement import *
from libs.dataMNGR import DATA_MNGR 
from libs.vehicule import * 
from libs.rapport import *
from libs.emplacement_voiture import *

"""from libs.emplacement_moto import * """
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from datetime import datetime
global donnees





def main():
    """ doc 
    sddg
    dsgd
    """
 
    
def option1():
    print("Option 1 choisie")
    # Création de la fenêtre principale
    global window1
    window1 = tk.Tk()
    window1.title("Authentication Window")
    global username
    global password 
# Éléments de l'interface utilisateur
    label_username = tk.Label(window1, text="Username:")
    label_password = tk.Label(window1, text="Password:")
    global entry_username 
    entry_username = tk.Entry(window1)
    global entry_password  # Masque les caractères du mot de passe
    entry_password = tk.Entry(window1, show="*")
    

# Placement des éléments dans la fenêtre
    label_username.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
    label_password.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
    entry_username.grid(row=0, column=1, padx=10, pady=5)
    entry_password.grid(row=1, column=1, padx=10, pady=5) 
    button_login = tk.Button(window1, text="Login",command=option3)
    button_login.grid(row=2, column=1, pady=10)
    window1.mainloop()

def option3():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        window1.destroy()
        #messagebox.showinfo("Authentication", "Authentication successful!")
        fenetre1()
        
    else:
        messagebox.showerror("Authentication Error", "Invalid username or password")
        print(username)
        print(password)
        window1.destroy()


def fenetre1():
    global window2
    window2 = tk.Tk()
    window2.geometry('300x300')
    window2.title("Admin options")
    button_park = tk.Button(window2, text="Park Vehicle", command=park_vehicle)
    button_leave = tk.Button(window2, text="Leave Parking",command=leave_parking)
    button_check = tk.Button(window2, text="Check Status",command=check_status)
    button_back = tk.Button(window2, text="Back", command=Back)  
    button_exit = tk.Button(window2, text="Exit", command= exit_application)
    button_park.place(x=100, y=50)
    button_leave.place(x=100, y=100)
    button_check.place(x=100, y=150)
    button_back.place(x=120, y=200)
    button_exit.place(x=120, y=250)
    window2.mainloop()

def park_vehicle():
    global window3
    window3 = tk.Tk()
    window3.title("Formulaire")
    window3.geometry('300x300')
    matricule_label = tk.Label(window3, text="Matricule")
    matricule_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    global matricule_entry
    matricule_entry = tk.Entry(window3)
    matricule_entry.grid(row=0, column=1, padx=10, pady=10)
    
# Ajout d'un champ pour le type de véhicule
    type_label = tk.Label(window3, text="Type")
    type_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    types = ["Voiture", "Moto", "Bateau", "Remorque"]
    global type_combobox
    type_combobox = ttk.Combobox(window3, values=types)
    type_combobox.grid(row=1, column=1, padx=10, pady=10)

    type_label_1 = tk.Label(window3, text="Niveau")
    type_label_1.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    types = ["Niveau0", "Niveau1", "Niveau2", "Niveau3"]
    global type_combobox1
    type_combobox1 = ttk.Combobox(window3, values=types)
    type_combobox1.grid(row=2, column=1, padx=10, pady=10)
    
# Ajout d'un champ pour le handicapé
    handicapped_label = tk.Label(window3, text="Handicapé")
    handicapped_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    types = ["Oui", "Non"]
    handicapped_var = tk.StringVar()
    global type_combobox2
    type_combobox2 = ttk.Combobox(window3, values=types)
    type_combobox2.grid(row=3, column=1, padx=10, pady=10)
   
# Ajout d'un bouton "OK" pour soumettre le formulaire
    ok_button = tk.Button(window3, text="OK",width=20, command=on_ok_button)
    ok_button.grid(row=4, column=1, columnspan=5, pady=10)

# Lancement de la boucle principale
    window3.mainloop()
    

def leave_parking():
    global window4
    window4 = tk.Tk()
    window4.title("Leave parking")
    window4.geometry('300x300')
    matricule_label = tk.Label(window4, text="Matricule")
    matricule_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    global matricule_entry1
    matricule_entry1 = tk.Entry(window4)
    matricule_entry1.grid(row=0, column=1, padx=10, pady=10)
    type_label = tk.Label(window4, text="Type")
    type_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    types = ["Voiture", "Moto", "Bateau", "Remorque"]
    global type_combobox1
    type_combobox1 = ttk.Combobox(window4, values=types)
    type_combobox1.grid(row=1, column=1, padx=10, pady=10)

    type_label_1 = tk.Label(window4, text="Niveau")
    type_label_1.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    types = ["Niveau0", "Niveau1", "Niveau2", "Niveau3"]
    global type_combobox11
    type_combobox11 = ttk.Combobox(window4, values=types)
    type_combobox11.grid(row=2, column=1, padx=10, pady=10)
    handicapped_label = tk.Label(window4, text="Handicapé")
    handicapped_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    types = ["Oui", "Non"]
    handicapped_var = tk.StringVar()
    global type_combobox22
    type_combobox22 = ttk.Combobox(window4, values=types)
    type_combobox22.grid(row=3, column=1, padx=10, pady=10)

    ok_button = tk.Button(window4, text="OK",width=20, command=on_ok_button2)
    ok_button.grid(row=4, column=1, columnspan=5, pady=10)

# Lancement de la boucle principale
    window4.mainloop()
def on_ok_button2():
    P1=Parking(50,1,0,0,0)

    try:

        a=matricule_entry1.get()#matricule
        b=type_combobox1.get()#type de voiture
        c=type_combobox11.get()#niveau
        d=type_combobox22.get()#handicapé?
        print(a,b,c,d)
        v=Vehicule(a,b)
        fich="data/"+c+".json"
        #C:\Users\siwar\OneDrive\Bureau\projet-PM 5\projet-PM\data
        with open(fich, 'r') as file:
            data = json.load(file)
        heure1,heure2=v.liberer_place(data["parking"],d)
        print(heure1,heure2)
        messagebox.showinfo("Ok", "voiture libérée")
        if c=="Niveau1":
            date_obj1 = datetime.fromisoformat(heure1)
            date_obj2 = datetime.fromisoformat(heure2)
            print(date_obj1,date_obj2)
            montant=P1.calculate_parking_cost(v, date_obj1,date_obj2)
              
            
            messagebox.showinfo("Payement", "Il faut payer"+str(montant)+"Euros")
            
        
        with open(fich, 'w') as fichier:
                        json.dump(data, fichier, indent=2)

        window4.destroy()
    except:
        messagebox.showerror("ERROR","Non trouvé")

    

def check_status():
    with open('data/Niveau0.json', 'r') as file:
        data = json.load(file)
    m="Niveau0"+"\n"+afficher_etat_parking(data["parking"])
    with open('data/Niveau1.json', 'r') as file:
        data = json.load(file)
    m+="\n"+"Niveau1"+"\n"+afficher_etat_parking(data["parking"])
    with open('data/Niveau2.json', 'r') as file:
        data = json.load(file)
    m+="\n"+"Niveau2"+"\n"+afficher_etat_parking(data["parking"])
    with open('data/Niveau3.json', 'r') as file:
        data = json.load(file)
    m+="\n"+"Niveau3"+"\n"+afficher_etat_parking(data["parking"])
    messagebox.showinfo("État du parking", m)
     

def Back():
    window2.destroy()

def exit_application():
    window2.destroy()
    fenetre.destroy()

def on_ok_button():
    a=matricule_entry.get()
    b=type_combobox.get()
    c=type_combobox1.get()
    d=type_combobox2.get()
    print(a,b,c,d)
    v=Vehicule(a,b)
    fich="data/"+c+".json"
    with open(fich, 'r') as file:
                data = json.load(file)
    try:
        numnum=v.enregistrer_entree_voiture(data["parking"],d)
        
        with open(fich, 'w') as fichier:
                    json.dump(data, fichier, indent=2)
        e=EmplacementVoiture(numnum,data["parking"]["occupied_places"])
        messagebox.showinfo("Parking System", e.have_spot_number()) # attribuer un num a la place ,,,dansla class emplacement voiture 
    except:
                messagebox.showerror("ERROR","Places occupées")
        


    
    window3.destroy()
    

def afficher_etat_parking(parking):
    nombre_places_disponibles = parking["available_places"]
    nombre_places_occupees = parking["occupied_places"]
    
    message = f"Nombre de places disponibles : {nombre_places_disponibles}\nNombre de places occupées : {nombre_places_occupees}"
    return message

    


    


    

def option2():
    with open('data/Niveau0.json', 'r') as file:
        data = json.load(file)
    m="Niveau0"+"\n"+afficher_etat_parking(data["parking"])
    with open('data/Niveau1.json', 'r') as file:
        data = json.load(file)
    m+="\n"+"Niveau1"+"\n"+afficher_etat_parking(data["parking"])
    with open('data/Niveau2.json', 'r') as file:
        data = json.load(file)
    m+="\n"+"Niveau2"+"\n"+afficher_etat_parking(data["parking"])
    with open('data/Niveau3.json', 'r') as file:
        data = json.load(file)
    m+="\n"+"Niveau3"+"\n"+afficher_etat_parking(data["parking"])
    messagebox.showinfo("État du parking", m)



# Création de la fenêtre principale
global fenetre
fenetre = tk.Tk()
fenetre.title("Parking Parkmetre")

# Configuration de l'arrière-plan
arriere_plan = tk.Canvas(fenetre, width=500, height=400, bg="orange")
arriere_plan.pack(fill=tk.BOTH, expand=True)

# Ajout du titre principal
titre_principal = tk.Label(fenetre, text="Bienvenue Au Parking Parkmetre", font=("Helvetica", 24), bg="orange")
titre_principal.place(x=20, y=20)

# Ajout du sous-titre
sous_titre = tk.Label(fenetre, text="Choisissez votre option", font=("Helvetica", 14), bg="orange")
sous_titre.place(x=150, y=100)

# Ajout des boutons
bouton_option1 = tk.Button(fenetre, text="Owner", command=option1)
bouton_option1.place(x=200, y=200)

bouton_option2 = tk.Button(fenetre, text="Employé", command=option2)
bouton_option2.place(x=200, y=250)

# Lancement de la boucle principale
fenetre.mainloop()




if __name__ == "__main__":
    main()
    
