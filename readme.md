# Simple Terminal Based Parking Lot Tracker Management System

# Application Requirements:

This Python terminal-based application allows you to manage a parking lot with two levels (A and B). Each level can park 20 vehicles of any size. The application supports the following operations:

   1. Automatically assign a parking space to a new vehicle.
   2. Retrieve parking spot number for a particular vehicle.

## How to Use the application

## Technical Requirements

- Python 3.x

- Git clone - git clone https://github.com/anirbanchakraborty123/Simple-Terminal-Based-Parking-Lot-Tracker--Management-Application.git

- Run the `RunApplication.py` script.
   - python RunApplication.py

## Modules

- `RunApplication.py`: The main application that interacts with the user.
- `vehicle.py`: Defines the `Vehicle` class.
- `parkingspot.py`: Defines the `ParkingSpot` class.
- `parkinglot.py`: Defines the `ParkingLot` class that manages parking spots.

## Choose an option:
   - Enter `1` to assign a parking spot to a new vehicle. You will be prompted to enter the vehicle number, and the application will assign a spot if available.
   - Enter `2` to retrieve the parking spot number for a vehicle. You will be prompted to enter the vehicle number, and the application will display the spot if the vehicle is parked.
   - Enter `3` to exit the program.

## Example

## Options:

Assign a parking spot to a new vehicle
Retrieve parking spot number for a vehicle
Exit
Enter your choice: 1
Enter the vehicle number: ABC123
Parking spot assigned: {"level": "A", "spot": 1}

## Options:

Assign a parking spot to a new vehicle
Retrieve parking spot number for a vehicle
Exit
Enter your choice: 2
Enter the vehicle number: XYZ789
Vehicle not found in the parking lot.

## Options:

Assign a parking spot to a new vehicle
Retrieve parking spot number for a vehicle
Exit
Enter your choice: 2
Enter the vehicle number: ABC123
Vehicle is parked at: {"level": "A", "spot": 1}

## Options:

Assign a parking spot to a new vehicle
Retrieve parking spot number for a vehicle
Exit
Enter your choice: 3
Exiting the program.