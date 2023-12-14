from libs.parking import Parking   

def main():
    """ doc 
    sddg
    dsgd
    """
    parking_lot = Parking()

    while True:
        print("\n--- Parking System Menu ---")
        print("1. Park Vehicle")
        print("2. Leave Parking")
        print("3. Check Status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                level = int(input("Enter the level to park the vehicle: "))
                vehicle_type = input("Enter the vehicle type (e.g., car, motorcycle): ")

                # Ask for duration only if the level is 1
                duration = None
                if level == 1:
                    duration = input("Enter the parking duration (hourly, daily): ")

                # Ask for handicapped only if the level is 0 or 1
                handicapped = False
                if level in [0, 1]:
                    handicapped_input = input("Is it a handicapped vehicle? (yes/no): ").lower()
                    handicapped = handicapped_input == "yes"

                result = parking_lot.park_vehicle(level, vehicle_type, duration, handicapped)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                level = int(input("Enter the level to leave the parking: "))
                spot_number = int(input("Enter the spot number to leave: "))
                result = parking_lot.leave_parking(level, spot_number)
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            print("\n--- Parking Status ---")
            for level, spots in parking_lot.occupied_spots.items():
                print(f"Level {level}: {spots.count(True)}/{len(spots)} spots occupied")

        elif choice == "4":
            print("Exiting the Parking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
    
