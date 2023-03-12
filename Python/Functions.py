def ReadFile(filename):
    """Reads a file and returns a list of tasks that are in the file"""
    with open(f"{filename}","r") as file:
            todo=file.readlines()
    return todo

def WriteFile(filename , data):
       """Write to the file the data that you provided"""
       with open(f"{filename}","w") as file:
            file.writelines(data)


        
