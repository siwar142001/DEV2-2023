

class Parking:
    def __init__(self):
        """
        Initialize parking lot with total capacity and levels.
        """
        self.total_capacity = 200
        self.levels = {
            0: {"type": "Resident Parking", "capacity": 50, "handicapped_capacity": 2},
            1: {"type": "Hourly/ Daily Parking", "capacity": 50, "handicapped_capacity": 2},
            2: {"type": "Garage Repair/Sales", "capacity": 50, "handicapped_capacity": 0},
            3: {"type": "Garage Repair/Sales", "capacity": 50, "handicapped_capacity": 0}
        }
        self.occupied_spots = {level: [False] * info["capacity"] for level, info in self.levels.items()}
        self.occupied_handicapped_spots = {level: [False] * (info["handicapped_capacity"] * 2) for level, info in self.levels.items() if info["handicapped_capacity"] > 0}
        self.occupied_motorcycle_spots = {level: [False] * info["capacity"] for level, info in self.levels.items()}
        self.vehicle_entries = []  # List to store vehicle entries



    def validate_level(self, level, handicapped=False):
        """
        Check if the given level is valid and supports handicapped parking.

        Args:
            level (int): The level to be validated.
            handicapped (bool, optional): Whether handicapped parking is required. Defaults to False.

        Returns:
            bool: True if the level is valid and supports handicapped parking; False otherwise.
        """
        if level not in self.levels:
            raise ValueError(f"Invalid level {level}.")

        if handicapped and self.levels[level]["handicapped_capacity"] == 0:
            raise ValueError(f"Level {level} does not support handicapped parking.")

        if handicapped and self.levels[level]["handicapped_capacity"] * 2 > self.levels[level]["capacity"]:
            raise ValueError(f"Not enough capacity for handicapped parking on level {level}.")
        return True

    def validate_spot_number(self, level, spot_number):
        """
        Validate if the provided spot number is valid for the given level.

        Args:
            level (int): The level on which the spot is located.
            spot_number (int): The spot number to be validated.

        Raises:
            ValueError: If the spot number is not valid for the given level.
        """
        if not (0 <= spot_number < self.levels[level]["capacity"]):
            raise ValueError(f"Invalid spot number {spot_number} for {self.levels[level]['type']}.")

    def calculate_total_revenue(self):
            total_revenue = 0.0
            for entry in self.vehicle_entries:
                if entry["level"] == 1 and entry["duration"] is not None:
                    total_revenue += self.calculate_parking_cost(entry["vehicle_type"], entry["duration"])
            return total_revenue

    def calculate_parking_cost(self, vehicle_type, duration, count):
        """
        Calculate the parking cost based on vehicle type, duration, and spot count.
        Args:
            duration (int): The parking duration in hours.
            count (int): The count of vehicles parked.
        Returns:
            float: The calculated parking cost.
        """
        hourly_rate = 2.0
        daily_rate = 48.0
        return hourly_rate + (count * 2.5) if duration < 24 else daily_rate

    def view_availability(self):
        """
        Display the availability on each level.
        """
        for level, spots in self.occupied_spots.items():
            available_spots = sum(not spot for spot in spots)
            print(f"Level {level}: {available_spots} spots available.")
    
    def display_reserved_spots(self):
        for entry in self.vehicle_entries:
            if entry.get("reservation", False):
                print(f"Reserved spot on Level {entry['level']} for {entry['vehicle_type']}")
