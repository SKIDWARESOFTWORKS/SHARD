
def checkforcode():

    if line == 'echoln':
        pass

inp = input('What file are you compiling?')

with open(inp, 'r') as file:
    
    for line in file:

        checkforcode()


# THIS FILE WILL BE CHANGED TO .EXE FILE LATER, THIS IS A TEMPORARY FILE
