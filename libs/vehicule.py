from datetime import datetime
import unittest

class Vehicule:
    """cette class définie qui peut etre voiture / moto /remorque/bateau"""
    def __init__(self, immatriculation, type_vehicule):
        self.immatriculation = immatriculation
        self.type_vehicule = type_vehicule
        self.date_entree = None
        self.date_sortie = None

    def __str__(self):
        return "la matricule de cette voiture est {} ".format(self.immatriculation)

    def enregistrer_entree_voiture(self,parking,h):
        """cette methode permet d'enregister l'entrée du vehicule dans le parking """
    # Trouver la première place disponible dans les places régulières
        if h=="Non" or h=="non" :
                for place in parking["regular_places"]:
                    if place["status"] == "available":
                        # Mettre à jour les détails de la place
                        place["status"] = "occupied"
                        place["car_license_plate"] = self.immatriculation
                        place["entry_time"] = datetime.now().isoformat()
                        self.date_entree= datetime.now().isoformat()
                        # Mettre à jour les compteurs de places
                        parking["occupied_places"] += 1
                        parking["available_places"] -= 1
                        numnum=place["id"]
                        return numnum # numero de la place
                    
        else:
            for place in parking["handicap_places"]:
                enregistre=False
                if place["status"] == "available"and enregistre==False:
                    # Mettre à jour les détails de la place
                    place["status"] = "occupied"
                    place["car_license_plate"] = self.immatriculation
                    place["entry_time"] = datetime.now().isoformat()
                    # Mettre à jour les compteurs de places
                    parking["occupied_places"] += 2
                    parking["available_places"] -= 2
                    numnum=place["id"]
                    return numnum
                
        return False
    def liberer_place(self,parking,h):
        """cette methode permet de libérer la place parking"""
        if h=="Non" or h=="non":
            print("on a commencé")
            for place in parking["regular_places"]:
                if place["car_license_plate"] == self.immatriculation and place["status"] == "occupied":
                    print("voiture touvé")
                # Mettre à jour les détails de la place
                    place["status"] = "available"
                    place["car_license_plate"] = None
                    h_entree=place["entry_time"]
                    place["entry_time"] = None
                
                # Mettre à jour les compteurs de places
                    parking["occupied_places"] -= 1
                    parking["available_places"] += 1
                
                # Retourner l'heure de sortie
                    self.date_sortie = datetime.now().isoformat()
                    return datetime.now().isoformat(), h_entree
    
    # Si la place n'a pas été trouvée dans les places régulières, chercher dans les places réservées aux handicapés
        else:
            for place in parking["handicap_places"]:
                if place["id"] == self.immatriculation and place["status"] == "occupied":
                    # Mettre à jour les détails de la place
                    place["status"] = "available"
                    place["car_license_plate"] = None
                    h_entree=place["entry_time"]
                    place["entry_time"] = None
                    
                    # Mettre à jour les compteurs de places
                    parking["occupied_places"] -= 1
                    parking["available_places"] += 1
                    
                    # Retourner l'heure de sortie
                    return datetime.now().isoformat(), h_entree



class test(unittest.TestCase) : 
    def test_str(self) : 
        v1=Vehicule("333","Voiture")
        v2=Vehicule("444","remorque")
        """Vérification de str"""
        self.assertEqual(str(v1), "la matricule de cette voiture est 333 ")
        self.assertEqual(str(v2), "la matricule de cette voiture est 444 ")
      
      
if __name__ == '__main__':

    unittest.main()