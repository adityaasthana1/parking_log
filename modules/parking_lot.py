class ParkingLot:

    # Constructor to initiate the class variables
    def __init__(self,number_of_slots):


        #[0,1,1,0]
        #number of slots to be added in the parking lot being created
        self.number_of_slots = int(number_of_slots)

        # This array is an hash array, which will be used to see if a certain position
        # from 0 to n-1 is occupied or not. 
        # We are following 1-based indexing in this application
        # so for slot 1 -> index will be 0
        self.occupied_hash = [0]*self.number_of_slots

        # This is the hashmap/key-value store to store the vehicle data in the key-value pair of (slot,vehicle_data)
        # This helps us access the slot and vehicle data directly without iterating.
        self.parking_map = {}

        #This variable is to track the number of cars overall parked in the parking lot.
        self.number_of_cars_parked = 0

    # Just a function to help debug the code
    # Prints all the variables of the class
    def printVariables(self):
        print('number of slots :',self.number_of_slots)
        print('occupied hash :',self.occupied_hash)
        print('parking map :',self.parking_map)
        print('number of cars parked :',self.number_of_cars_parked)


    # This function finds the closest available/unoccupied slot from the start
    def findClosestIndex(self):
        
        # Simple iteration over the occupied_hash array from the beginning to check which one's available or '0'
        for i in range(0,self.number_of_slots):
            if self.occupied_hash[i] == 0:
                return i
        
        return -1


    # Function to park the vehicle in parking lot
    def park(self,vehicle_registration_number,vehicle_color):
        #Check if the parking lot is full
        if self.number_of_cars_parked == self.number_of_slots:
            print("ERROR PARKING LOT FULL : The parking lot is full!")
        else:
            # Find the closest slot available in the lot using occupied_hash array
            closest_slot = self.findClosestIndex()

            # Add the car in the parking lot
            # mark the position of parking as parked or '1' 
            self.occupied_hash[closest_slot] = 1
            
            # increase the number of vehicles parked in the parking lot
            self.number_of_cars_parked = self.number_of_cars_parked + 1

            # push the (slot,vehicle) data into our key-value store
            self.parking_map[closest_slot] = {
                'registration_number' : vehicle_registration_number,
                'vehicle_color' : vehicle_color
            }

            # print operation success
            print('vehicle',vehicle_registration_number,'parked in slot',(closest_slot+1))


    '''
    NOTE : We are using 1 based indexing here.
    So remember to increment values by 1 when printing
    '''
    # Function to remove the vehicle from a slot and parking lot
    def leave(self,slot_number):
        # Check if given slot is out of bound
        if slot_number > self.number_of_slots:
            print("Please enter a valid slot number")
        
        # Check if the slot is actually occupied or not 
        elif slot_number not in self.parking_map:
            print("There is no car parked here, Can not leave")

        # remove vehicle from slot operation
        else:
            # remove the (slot,vehicle) data from the key-value store
            del self.parking_map[slot_number-1]

            # decrement the number of cars in the parking lot by 1
            self.number_of_cars_parked = self.number_of_cars_parked - 1

            # mark the slot as unoccupied/available or '0' 
            self.occupied_hash[slot_number-1] = 0

            # operation success confirmation
            print('vehicle successfully left from slot',slot_number)


    # prints the current state of the parking lot
    def status(self):
        print("--------------------------STATUS--------------------------------")
        print('total vehicles in the parking lot :' , self.number_of_cars_parked,"\n\nThey are:")
        # Iterate through the all the keys in key-value store/hashmap and print the data.
        for slot in self.parking_map:
            print("Slot number:", (int(slot) + 1), "  Vehicle Registration Number:", self.parking_map[slot]['registration_number'], "  Vehicle Color:" , self.parking_map[slot]['vehicle_color'])
        
        print("---------------------------------------------------------------")


    # prints the list of vehicles with a specific color
    def findVehiclesWithColor(self,color):
        filtered_list = []
        for slot in self.parking_map:
            if self.parking_map[slot]['vehicle_color'] == color:
                filtered_list.append(self.parking_map[slot]['registration_number'])
        
        print("----------------------VEHICLES OF COLOR----------------------------")
        print('Color:' , color, '\nThey are:')
        if len(filtered_list) == 0:
            print("There are no cars with color",color)
        else:
            for item in filtered_list:
                print(item)
        print("-------------------------------------------------------------------")
        
    
    # prints all the slots for cars of particular color
    def findSlotsForCarsWithColor(self,color):
        filtered_list = []
        for slot in self.parking_map:
            if self.parking_map[slot]['vehicle_color'] == color:
                slot_text = "slot " + str(slot) 
                filtered_list.append(slot_text)
        
        print("------------------------SLOTS OF COLOR-----------------------------")
        print('Color:' , color, '\nThey are:')
        if len(filtered_list) == 0:
            print("There are no cars with color",color)
        else:
            for item in filtered_list:
                print(item)
        print("-------------------------------------------------------------------")

    

    # prints the slot of vehicle of particular registration number
    def findSlotWithRegistrationNumber(self,registration_number):
        
        print("------------------------SLOT WITH CAR REGISTRATION NO-----------------------------")
        for slot in self.parking_map:
            if self.parking_map[slot]['registration_number'] == registration_number:
                print('The car with registration number',registration_number,'is parket at slot',slot)    
                print("----------------------------------------------------------------------------------") 
                return
        
        print('The car with registration number',registration_number,'wasnt found in our parking')
        print("----------------------------------------------------------------------------------")