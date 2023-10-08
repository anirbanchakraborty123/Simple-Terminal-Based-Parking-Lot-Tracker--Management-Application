from Parking_lot.vehicle import Vehicle
from Parking_lot.parking_spot import ParkingSpot
from Parking_lot.parking_lot import ParkingLot

# Simple menu-based system to interact with the parking lot.

if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("1. Park a vehicle")
        print("2. Retrieve parking spot for a vehicle")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            vehicle = Vehicle(vehicle_number)
            spot = parking_lot.assign_spot(vehicle)
            if spot:
                print(f"Parked at Level {spot['level']}, Spot {spot['spot']}")
            else:
                print("Parking lot is full!")

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            spot = parking_lot.retrieve_spot(vehicle_number)
            if spot:
                print(f"Level {spot['level']}, Spot {spot['spot']}")
            else:
                print("Vehicle not found in the parking lot.")

        elif choice == "3":
            break
