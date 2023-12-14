import json
import os

class DATA_MNGR : 
        
    def add_to_json(self, filename="C:/Users/siwar/OneDrive/Bureau/projet-PM/data/vehicle_entries.json"):
        """
        Save the list of vehicle entries to a JSON file.

        Args:
            filename (str, optional): The name of the JSON file. Defaults to "vehicle_entries.json".
        """
        entries_data = {
            "total_capacity": self.total_capacity,
            "occupied_spots": self.occupied_spots,
            "occupied_handicapped_spots": self.occupied_handicapped_spots,
            "occupied_motorcycle_spots": self.occupied_motorcycle_spots,
            "vehicle_entries": self.vehicle_entries
        }

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "a") as json_file:
            json.dump(entries_data, json_file)
            
     
    def remove_vehicle_entry(self, level, spot_number):
            """
            Remove the entry of the vehicle from self.vehicle_entries.

            Args:
                level (int): The level from which the vehicle is leaving.
                spot_number (int): The spot number from which the vehicle is leaving.

            Returns:
                str: A message indicating the removed vehicle.
        """
            for i, entry in enumerate(self.vehicle_entries):
                if entry["level"] == level and entry.get("spot_number", None) == spot_number:
                    removed_vehicle = self.vehicle_entries.pop(i)
                    self.add_to_json()  # Update the JSON file
                    return f"Vehicle removed: {removed_vehicle}"
            return "Vehicle entry not found."
