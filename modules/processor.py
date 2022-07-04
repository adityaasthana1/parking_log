import modules.parking_lot as pl

class CommandProcessor:
    
    # Constructor to initialize class variables
    def __init__(self): 

        # TAGS to represent any input command
        self.CREATE_PARKING_LOT = 'create_parking_lot'       
        self.PARK = 'park'
        self.LEAVE = 'leave'
        self.STATUS = 'status'
        self.REGISTRATION_NUMBERS_OF_COLOR = 'registration_numbers_for_cars_with_colour'
        self.SLOT_NUMBER_OF_COLOR = 'slot_numbers_for_cars_with_colour'
        self.SLOT_NUMBER_OF_REGISTRATION_NUMBER = 'slot_number_for_registration_number'
        self.PRINTVAR = 'printvar'
        self.LIST_COMMANDS = 'list_commands'
        self.EXIT = 'exit'

        # ParkingLot class instance initialized to NULL or None
        self.parkingLot = None


    # End function that takes line(string) and split all the words to a list or command set, to be further processed.
    def processCommand(self,inputCommand):
        # split the given line into list
        command_set = inputCommand.split()
        self.resolveCommandAndExecute(command_set)
        

    # Function to resolve the command out from the command set given.
    def resolveCommandAndExecute(self,command_set):

        # Just in case we are given with an empty command
        if len(command_set) == 0:
            print("Command cannot be empty")
            return

        #The 0th index of each command set will be our primary keyword that defines a task.
        keyword = command_set[0]
    
        if keyword == self.CREATE_PARKING_LOT:
            if len(command_set) != 2: # Valid number of arguments check
                print("ERROR : PARKING_LOT NOT CREATED :\nplease enter valid set of arguments")
                return
            elif self.parkingLot != None: # Checking wether parking lot exists or not
                print('ERROR : PARKING_LOT already exists')
            elif not command_set[1].isnumeric(): # Checking wether the given input argument as parameter is numeric or not
                print('ERROR : ENTER VALID PARAMETER:\nThe input should be a positive integer')
            else:
                lot_size = command_set[1]
                self.parkingLot = pl.ParkingLot(lot_size)
                print("Parking lot of size:",lot_size," created successfully!" )

            
        elif keyword == self.PARK:
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            elif len(command_set) != 3:
                print("ERROR : VEHICLE_NOT_PARKED :\nVehicle is not parked. Please enter valid set of arguments.")
            else:
                vehicle_registration_number = command_set[1]
                vehicle_color = command_set[2]
                self.parkingLot.park(vehicle_registration_number,vehicle_color)

        elif keyword == self.LEAVE:
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            elif len(command_set) != 2:
                print("ERROR : PARKING_LOT NOT CREATED :\nplease enter valid set of arguments")
            elif not command_set[1].isnumeric():
                print('ERROR : ENTER VALID PARAMETER:\nThe input should be a positive integer')
            else:
                slot_number = command_set[1]
                self.parkingLot.leave(int(slot_number)) 

        elif keyword == self.STATUS:
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            else:
                self.parkingLot.status()
            

        elif keyword == self.REGISTRATION_NUMBERS_OF_COLOR:
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            elif len(command_set) != 2:
                print("ERROR : INVALID ARGUMENTS :\nplease enter valid set of arguments")
            else:
                self.parkingLot.findVehiclesWithColor(command_set[1])

        elif keyword == self.SLOT_NUMBER_OF_COLOR:
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            elif len(command_set) != 2:
                print("ERROR : INVALID ARGUMENTS :\nplease enter valid set of arguments")
            else:
                self.parkingLot.findSlotsForCarsWithColor(command_set[1])
        elif keyword == self.SLOT_NUMBER_OF_REGISTRATION_NUMBER:
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            elif len(command_set) != 2:
                print("ERROR : INVALID ARGUMENTS :\nplease enter valid set of arguments")
            else:
                self.parkingLot.findSlotWithRegistrationNumber(command_set[1])
            
        elif keyword == self.PRINTVAR:
            if self.parkingLot is not None:
                self.parkingLot.printVariables()
            else:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
                
        elif keyword == self.LIST_COMMANDS:
            print('-----------------------------------------------LIST OF COMMANDS-------------------------------------------------')
            print('1. create_parking_lot <number_of_slots> : Create parking lot of size: number_of_slots.')
            print('2. park <vehicle_number> <vehicle_color> : Park a vehicle in the nearest slot from the start.')
            print('3. leave <slot_number> : A vehicle leaves an occupied slot and leaves the parking.')
            print('4. status : List all the car parking scheme')
            print('5. registration_numbers_for_cars_with_colour <color_name> : List all car registration numbers with the given color.')
            print('6. slot_numbers_for_cars_with_colour <color_name> : List the slots which have the car of given color.')
            print('7. slot_number_for_registration_number <registration_number> : List the slot number of the given car.')
            print('8. printvar : Print the ParkingLot class variables to get the execution insight')
            print('9. list_commands : List all the available commands')
            print('----------------------------------------------------------------------------------------------------------------')

        else:
            print('ERROR : keyword \'', keyword, '\' is not a valid keyword.\nUse list_commands command to see all available commands' )

        
    