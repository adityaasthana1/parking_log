class ParkingLot:

    def __init__(self,number_of_slots):
        self.number_of_slots = int(number_of_slots)
        self.occupied_hash = [0]*self.number_of_slots
        self.parking_map = {}
        self.number_of_cars_parked = 0

    def printVariables(self):
        print('number of slots :',self.number_of_slots)
        print('occupied hash :',self.occupied_hash)
        print('parking map :',self.parking_map)
        print('number of cars parked :',self.number_of_cars_parked)

    def findClosestIndex(self):
        for i in range(0,self.number_of_slots):
            if self.occupied_hash[i] == 0:
                return i
        
        return -1

    def park(self,vehicle_registration_number,vehicle_color):
        if self.number_of_cars_parked == self.number_of_slots:
            print("ERROR PARKING LOT FULL : The parking lot is full!")
        else:
            closest_slot = self.findClosestIndex()
            self.occupied_hash[closest_slot] = 1
            self.number_of_cars_parked = self.number_of_cars_parked + 1
            self.parking_map[closest_slot] = {
                'registration_number' : vehicle_registration_number,
                'vehicle_color' : vehicle_color
            }
            