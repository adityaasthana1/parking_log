import modules.parking_lot as pl

class CommandProcessor:
    
    def __init__(self): 
        self.CREATE_PARKING_LOT = 'create_parking_lot'       
        self.PARK = 'park'
        self.LEAVE = 'leave'
        self.STATUS = 'status'
        self.REGISTRATION_NUMBERS_OF_COLOR = 'registration_numbers_for_cars_with_colour'
        self.SLOT_NUMBER_OF_COLOR = 'slot_numbers_for_cars_with_colour'
        self.SLOT_NUMBER_OF_REGISTRATION_NUMBER = 'slot_number_for_registration_number'
        self.parkingLot = None

    def processCommand(self,inputCommand):
        command_set = inputCommand.split()
        self.resolveCommandAndExecute(command_set)
        
    def resolveCommandAndExecute(self,command_set):
        keyword = command_set[0]

        if keyword == self.CREATE_PARKING_LOT:

            if len(command_set) != 2:
                print("ERROR : PARKING_LOT NOT CREATED :\nplease enter valid set of arguments")
                return
            elif self.parkingLot != None:
                print('ERROR : PARKING_LOT already exists')
            elif not command_set[1].isnumeric():
                print('ERROR : ENTER VALID PARAMETER:\nThe input should be a positive integer')
            else:
                lot_size = command_set[1]
                self.parkingLot = pl.ParkingLot(lot_size)
                print("Parking lot of size:",lot_size," created successfully!" )

            
        elif keyword == self.PARK:
            print(keyword)
            if self.parkingLot == None:
                print('ERROR : PARKING_LOT_NOT_EXIST:\nParking lot does not exist. Please create one first.')
            elif len(command_set) != 3:
                print("ERROR : PARKING_LOT NOT CREATED :\nplease enter valid set of arguments")
            else:
                vehicle_registration_number = command_set[1]
                vehicle_color = command_set[2]
                self.parkingLot.park(vehicle_registration_number,vehicle_color)
                self.parkingLot.printVariables()

        elif keyword == self.LEAVE:
            print(keyword)
        elif keyword == self.STATUS:
            print(keyword)
        elif keyword == self.REGISTRATION_NUMBERS_OF_COLOR:
            print(keyword)
        elif keyword == self.SLOT_NUMBER_OF_COLOR:
            print(keyword)
        elif keyword == self.SLOT_NUMBER_OF_REGISTRATION_NUMBER:
            print(keyword)
        else:
            print('ERROR : keyword \'', keyword, '\' is not a valid keyword' )

        
    