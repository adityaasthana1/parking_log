import sys
import modules.processor as cp


processor = cp.CommandProcessor()

try:
    # If the file is passed as an argument, We will try to open it and read the file
    with open(sys.argv[1], 'r') as f:
        list_of_commands = []
        for line in f:
            stripped_line = line.strip() #Strip all the lines in the file 
            list_of_commands.append(stripped_line)
            '''
            line_list = stripped_line.split()
            list_of_command_set.append(line_list)
            '''
        
        for command in list_of_commands:
            processor.processCommand(command)

       
except: 
    while 1:
        inputCommand = input('Enter A Command : ')
        processor.processCommand(inputCommand = inputCommand)