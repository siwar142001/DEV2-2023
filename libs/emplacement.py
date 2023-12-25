import random 


class Emplacement : 
    """ doc
    Args:
            level (int)
            """
    
    def __init__(self, spot_number , occupied_spots,vehicle_type):
        self.spot_number = spot_number
        self.occupied_spots = occupied_spots
        self.vehicle_type = vehicle_type
        
     
    def park_vehicle(self, level, vehicle_type, duration=None, handicapped=False):
        """
        Park a vehicle on the specified level.

        Args:
            level (int): The level on which to park the vehicle.
            vehicle_type (str): The type of the vehicle to be parked.
            duration (str, optional): The duration for parking (e.g., "hourly", "daily", "annual"). Defaults to None.
            handicapped (bool, optional): Whether handicapped parking is required. Defaults to False.
        """
        if not self.validate_level(level, handicapped):
            return True  # Automatically raises the error if the conditions are not met in the def validate_level.
        if handicapped:
            result = self.park_handicapped(level, vehicle_type)
        elif level == 1:
            result = self.park_level_1(vehicle_type, duration)
        else:
            result =  self.park_other_level(level, vehicle_type)
        
        self.vehicle_entries.append({
            "level": level,
            "vehicle_type": vehicle_type,
            "duration": duration,
            "handicapped": handicapped
        })
        self.add_to_json()

        return  result
    def park_other_level(self, level, vehicle_type):
        """
        Sorting parking lot for non-level 1, and for all kinds of vehicles.

        Args:
            level (int): The level on which to park the vehicle.
            vehicle_type (str): The type of the vehicle to be parked.

        Returns:
            str: A message indicating the result of the parking attempt.
        """
        try:
            for i, count in enumerate(self.occupied_motorcycle_spots[level]):
                if vehicle_type == "motorcycle" and count < 2:
                    self.occupied_spots[level][i] += 1
                    self.occupied_motorcycle_spots[level][i] += 1
                    return f"A {vehicle_type} is parked on {self.levels[level]['type']}, spot {i}"

            for i, occupied in enumerate(self.occupied_spots[level]):
                if not occupied:
                    self.occupied_spots[level][i] = True
                    return f"A {vehicle_type} is parked on {self.levels[level]['type']}, spot {i}"

            raise ValueError(f"No available spots on {self.levels[level]['type']} for {vehicle_type}.")
        except ValueError as e:
            return str(e)


    def park_level_1(self, vehicle_type, duration):
        """
        Park a vehicle in the Hourly and Daily Parking on level 1.

        Args:
            vehicle_type (str): The type of the vehicle to be parked.
            duration (str): The duration for parking (e.g., "hourly", "daily").
        """
        if duration is None:
            raise ValueError("Please specify the parking duration for level 1.")

        hourly_rate = 2.0
        daily_rate = 48.0

        for i, count in enumerate(self.occupied_motorcycle_spots[1]):
            if vehicle_type == "motorcycle" and count < 2:
                self.occupied_spots[1][i] += 1
                self.occupied_motorcycle_spots[1][i] += 1

                if duration == "hourly":
                    cost = hourly_rate + (count * 2.5)  # First hour is $2, then $2.5 for each additional hour
                    return(f"A {vehicle_type} (hourly) is parked on {self.levels[1]['type']}, spot {i}. Cost: ${cost:.2f}")
                elif duration == "daily":
                    return(f"A {vehicle_type} (daily) is parked on {self.levels[1]['type']}, spot {i}. Cost: ${daily_rate}")
                else:
                    raise ValueError(f"Invalid duration '{duration}' for parking on level 1")


        if duration == "hourly":
            for i, occupied in enumerate(self.occupied_spots[1][25:]):
                if not occupied:
                    spot_number = 25 + i
                    self.occupied_spots[1][spot_number] = True
                    cost = hourly_rate + (i * 2.5)  # First hour is $2, then $2.5 for each additional hour
                    return(f"A {vehicle_type} (hourly) is parked on {self.levels[1]['type']}, spot {spot_number}. Cost: ${cost:.2f}")
                    
            raise ValueError(f"No available hourly parking spots on {self.levels[1]['type']} for {vehicle_type}.")

        elif duration == "daily":
            for i, occupied in enumerate(self.occupied_spots[1][25:]):
                if not occupied:
                    spot_number = 25 + i
                    self.occupied_spots[1][spot_number] = True
                    return(f"A {vehicle_type} (daily) is parked on {self.levels[1]['type']}, spot {spot_number}. Cost: ${daily_rate}")
                    
            raise ValueError(f"No available daily parking spots on {self.levels[1]['type']} for {vehicle_type}.")

    
    def leave_parking(self, level, spot_number):
        """
        Remove a vehicle from the specified spot on the level.

        Args:
            level (int): The level from which to remove the vehicle.
            spot_number (int): The spot number from which to remove the vehicle.
        """
        if not self.validate_level(level):
            return True

        self.validate_spot_number(level, spot_number)

        if self.occupied_motorcycle_spots[level][spot_number] > 0:

            # If motorcycles share the spot, randomly choose which one is leaving
            motorcycle_count = self.occupied_motorcycle_spots[level][spot_number]
            motorcycle_to_leave = random.randint(1, motorcycle_count)

            # If motorcycles share the spot, decrement the count
            self.occupied_motorcycle_spots[level][spot_number] -= 1
            return(f"Motorcycle {motorcycle_to_leave} left {self.levels[level]['type']}, spot {spot_number}")

        elif self.occupied_spots[level][spot_number]:
            self.occupied_spots[level][spot_number] = False
            return(f"Vehicle left {self.levels[level]['type']}, spot {spot_number}")

        else:
            return(f"No vehicle at {self.levels[level]['type']}, spot {spot_number}")
 