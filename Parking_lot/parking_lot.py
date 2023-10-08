from Parking_lot.parking_spot import ParkingSpot

class ParkingLot:
    
    """  This class manages the parking spots on both levels A and B  """
    
    def __init__(self): 
        """ Constructor to initialize ParkingLot class """
        self.level_a_spots = [ParkingSpot(i, 'A') for i in range(1, 21)]
        self.level_b_spots = [ParkingSpot(i, 'B') for i in range(21, 41)]

    def assign_spot(self, vehicle):
        """ Function to assign parking spot to vehicle """
        
        for spot in self.level_a_spots + self.level_b_spots:
            if not spot.occupied:
                spot.park_vehicle(vehicle)
                vehicle.parking_spot = spot
                return {"level": spot.level, "spot": spot.spot_number}
        return None

    def retrieve_spot(self, vehicle_number):
        """ Function to retreive parking spot of vehicle """
        
        for spot in self.level_a_spots + self.level_b_spots:
            if spot.occupied and spot.vehicle.vehicle_number == vehicle_number:
                return {"level": spot.level, "spot": spot.spot_number}
        return None
