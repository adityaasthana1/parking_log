import sys
import modules.processor as cp


processor = cp.CommandProcessor()

def startListening():
    while 1:
        inputCommand = input('Enter A Command : ')
        processor.processCommand(inputCommand = inputCommand)

try:
    '''
    If the file is passed as an argument, We will try to open it and read the file

    '''
    with open(sys.argv[1], 'r') as f:
        list_of_commands = []
        for line in f:
            stripped_line = line.strip() #Strip all the lines in the file 
            list_of_commands.append(stripped_line) # Add all the lines to the list_of_commands
            
        
        '''
        We iterate through all the commands in the created list and execute it
        We use processCommand() from CommandProcessor class to perform execution 
        '''
        for command in list_of_commands:
            processor.processCommand(command)

    startListening()
       
except: 
    startListening()