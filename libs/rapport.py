from datetime import datetime
import json

class Rapport:
    """la classe Rapport est une classe qui permet de consulter et d'afficher
    l'état de tous les parking""" 
    def __init__(self):
        self.date = datetime.now()
        self.donnees = ""

    def generer_rapport(self,parking):
        """Cette méthode génére le rapport de lapart d'un parking donné"""
        nombre_places_disponibles = parking["available_places"]
        nombre_places_occupees = parking["occupied_places"]
        message = f"Nombre de places disponibles : {nombre_places_disponibles}\nNombre de places occupées : {nombre_places_occupees}"
        return message
    def consulter_rapport(self):
        """cette methode permet de consulter l'etat de tous les niveaux de parking"""
        with open('data/Niveau0.json', 'r') as file:
            data = json.load(file)
        m=str(self.date)+"\n"+"Niveau0"+"\n"+self.generer_rapport(data["parking"])
        with open('data/Niveau1.json', 'r') as file:
            data = json.load(file)
        m+="\n"+"Niveau1"+"\n"+self.generer_rapport(data["parking"])
        with open('data/Niveau2.json', 'r') as file:
            data = json.load(file)
        m+="\n"+"Niveau2"+"\n"+self.generer_rapport(data["parking"])
        with open('data/Niveau3.json', 'r') as file:
            data = json.load(file)
        m+="\n"+"Niveau3"+"\n"+self.generer_rapport(data["parking"])
        return m


