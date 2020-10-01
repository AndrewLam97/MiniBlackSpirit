#Sanitizes inputs
def sanitize(inputstr):
    return remove_command(inputstr).upper()

#Removes command keyword from input string
def remove_command(inputstr):
    try:
        partitionedstr = inputstr.partition(' ')
        print (partitionedstr[2])
        return partitionedstr[2]
    except:
        print("Something went wrong during sanitization")