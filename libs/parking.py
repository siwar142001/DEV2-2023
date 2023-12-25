
from datetime import datetime
class Parking:
    def __init__(self, total_capacity,level,occupied_spots,occupied_handicapped_spots,occupied_motorcycle_spots):
        """
        Initialize parking lot with total capacity and levels.
        """
        self.total_capacity = total_capacity
        self.levels =level
        self.occupied_spots =occupied_spots
        self.occupied_spots =occupied_spots
        self.occupied_handicapped_spots =occupied_handicapped_spots
        self.occupied_motorcycle_spots=occupied_motorcycle_spots

    def calculate_parking_cost(self, vehicle, h1,h2):
        """
        Calculate the parking cost """
        n=h1 - h2
        hours, remainder = divmod(n.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        if remainder!=0:
                hours+=1
        if hours==1:montant=2
        else:montant=2+(hours-1)*2.5
        return montant
        


    """def calculate_total_revenue(self):
            total_revenue = 0.0
            for entry in self.vehicle_entries:
                if entry["level"] == 1 and entry["duration"] is not None:
                    total_revenue += self.calculate_parking_cost(entry["vehicle_type"], entry["duration"])
            return total_revenue"""


    """def view_availability(self):

        for level, spots in self.occupied_spots.items():
            available_spots = sum(not spot for spot in spots)
            print(f"Level {level}: {available_spots} spots available.")
    
    def display_reserved_spots(self):
        for entry in self.vehicle_entries:
            if entry.get("reservation", False):
                print(f"Reserved spot on Level {entry['level']} for {entry['vehicle_type']}")
    """