


class Emplacement : 
    """ cette class permet de definir un emplacement (le numero_place et le pourcentage d'occupation)
            """
    
    def __init__(self, numero_place , occupied_spots):
        self.spot_number = numero_place
        self.occupied_spots = occupied_spots   
    


class EmplacementMoto(Emplacement): 
    """cette class permet de reserver un emplacement pour une moto"""
    def __init__(self, numero_place , occupied_spots):
         super.__init__(numero_place, occupied_spots)
         self.vehicle_type = "moto"
         
    def occuper_place(self,n):
        self.numero_place = n
        self.occupied_spots = 1/2
        
    def liberer_place(self): 
        if  self.occupied_spots == 1 :
            self.occupied_spots =1/2
        else :
            self.occupied_spots =0

