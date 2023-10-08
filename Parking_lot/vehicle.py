class Vehicle:
    """ Vehicle class to represent each vehicles. Each vehicle will have a unique 
        identifier (e.g., vehicle number), which will be used to retrieve its 
        parking spot.  
    """
    def __init__(self, vehicle_number):
        """ Constructor to initialize Vehicle class that takes 1 argument: vehicle_number """
        self.vehicle_number = vehicle_number
        self.parking_spot = None

    def getVehicleInfo(self):
        """ To get each vehicle informartion and its parking status"""
        if self.parking_spot:
            return self.vehicle_number + " is parked in "+self.parking_spot
        else:
            return self.vehicle_number + " is not parked here."
    
    