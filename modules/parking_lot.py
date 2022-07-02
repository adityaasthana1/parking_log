class ParkingLot:

    def __init__(self,number_of_slots):
        self.number_of_slots = int(number_of_slots)
        self.occupied_hash = [0]*self.number_of_slots
        self.parking_map = {}

    def printVariables(self):
        print(self.number_of_slots,self.occupied_hash,self.parking_map)
        