class ParkingSpot:
    """ ParkingSpot Class to represent individual parking spots. 
        Each spot will have a spot number and a level identifier."""
    
    def __init__(self, spot_number, level):
        """ Constructor to initialize ParkingSpot class
            that takes 2 arguments : spot_number and level """
        self.spot_number = spot_number
        self.level = level
        self.occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle):
        """ Function to park vehicle by taking vehicle object as an argument"""
        self.occupied = True
        self.vehicle = vehicle

    def vacate_spot(self):
        """ Function to vacate the occupied parking spot """
        self.occupied = False
        self.vehicle = None
