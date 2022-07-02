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
    
    '''
    NOTE : We are using 1 based indexing here.
    So remember to increment values by 1 when printing
    '''
    def leave(self,slot_number):
        if slot_number > self.number_of_slots:
            print("Please enter a valid slot number")
        elif slot_number not in self.parking_map:
            print("There is not car parked here, Can not leave")
        else:
            del self.parking_map[slot_number-1]
            self.number_of_cars_parked = self.number_of_cars_parked - 1
            self.occupied_hash[slot_number-1] = 0


    def status(self):
        print("--------------------------STATUS--------------------------------")
        print('total vehicles in the parking lot :' , self.number_of_cars_parked,"\n\nThey are:")
        for slot in self.parking_map:
            print("Slot number:", (int(slot) + 1), "  Vehicle Registration Number:", self.parking_map[slot]['registration_number'], "  Vehicle Color:" , self.parking_map[slot]['vehicle_color'])
        
        print("---------------------------------------------------------------")