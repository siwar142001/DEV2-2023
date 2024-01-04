

class Emplacement : 
    """ cette class permet de definir un emplacement (le numero_place et le pourcentage d'occupation)
            """
    
    def __init__(self, numero_place , occupied_spots):
        self.spot_number = numero_place
        self.occupied_spots = occupied_spots   
    

     
class EmplacementVoiture(Emplacement):  
    """cette class permet de reserver un emplacement pour les autres types de vehicules """
    def __init__(self, numero_place , occupied_spots,handicap):
        super.__init__(numero_place, occupied_spots)
        self.vehicle_type = "voiture"
        self .handicap=handicap
         
    def occuper_place(self,n):
        self.numero_place = n
        self.occupied_spots = 1
        
    def liberer_place(self):   
        self.occupied_spots =0
        
        
        