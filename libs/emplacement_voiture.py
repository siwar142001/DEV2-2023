from libs.emplacement import Emplacement 

class EmplacementVoiture(Emplacement):
    def __init__(self, spot_number , occupied_spots,vehicle_type="car"):
        super().__init__(spot_number , occupied_spots,vehicle_type="car")
        
        


    def have_spot_number(self):
        """
        Park a handicapped vehicle on the specified level.

        Args:
            level (int): The level on which to park the handicapped vehicle.
            vehicle_type (str): The type of the handicapped vehicle to be parked.
        """
        return "Vehicle parked successfully à la place "+str(self.spot_number)
   
