class CommandProcessor:
    def __init__(self): 
        self.CREATE_PARKING_LOT = 'create_parking_lot'       
        self.PARK = 'park'
        self.LEAVE = 'leave'
        self.STATUS = 'status'
        self.REGISTRATION_NUMBERS_OF_COLOR = 'registration_numbers_for_cars_with_colour'
        self.SLOT_NUMBER_OF_COLOR = 'slot_numbers_for_cars_with_colour'
        self.SLOT_NUMBER_OF_REGISTRATION_NUMBER = 'slot_number_for_registration_number'


    def processCommand(self,inputCommand):
        command_set = inputCommand.split()
        self.resolveCommandAndExecute(command_set)
        
    def resolveCommandAndExecute(self,command_set):
        keyword = command_set[0]

        if keyword == self.CREATE_PARKING_LOT:
            print(keyword)
        elif keyword == self.PARK:
            print(keyword)
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

        
