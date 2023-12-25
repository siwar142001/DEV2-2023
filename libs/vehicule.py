from datetime import datetime

class Vehicule:
    def __init__(self, immatriculation, type_vehicule):
        self.immatriculation = immatriculation
        self.type_vehicule = type_vehicule
        self.date_entree = None
        self.date_sortie = None



    def enregistrer_entree_voiture(self,parking,h):
    # Trouver la première place disponible dans les places régulières
        if h=="Non":
                for place in parking["regular_places"]:
                    if place["status"] == "available":
                        # Mettre à jour les détails de la place
                        place["status"] = "occupied"
                        place["car_license_plate"] = self.immatriculation
                        place["entry_time"] = datetime.now().isoformat()
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
        if h=="Non":
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
