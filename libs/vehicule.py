from datetime import datetime

class Vehicule:
    def __init__(self, immatriculation, type_vehicule):
        self.immatriculation = immatriculation
        self.type_vehicule = type_vehicule
        self.date_entree = None
        self.date_sortie = None

    def enregistrer_date_entree(self):
        self.date_entree = datetime.now()

    def enregistrer_date_sortie(self):
        self.date_sortie = datetime.now()