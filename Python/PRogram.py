import time


def ReadFile(filename):
    """Reads a file and returns a list of tasks that are in the file"""
    with open(f"{filename}","r") as file:
            todo=file.readlines()
    return todo

def WriteFile(filename , data):
       """Write to the file the data that you provided"""
       with open(f"{filename}","w") as file:
            file.writelines(data)

print("Your To do list: \n")

while True:
    print("Would you like to add, remove or see an item add remove see o exit: \n")
    whatToAcces =  input()
    whatToAcces= whatToAcces.strip()
    if whatToAcces.startswith('add'):
            item = whatToAcces.replace('add ','',1)+"\n"
            item=item.title()

            todo=ReadFile("data.txt")

            todo.append(item) 

            WriteFile("data.txt",todo)

    elif whatToAcces.startswith('remove'):
             item =  int(whatToAcces[7:])
             item-=1

             todo=ReadFile("data.txt")
             
             print(f"removed the task {todo[item]}")
             todo.pop(item)

             WriteFile("data,txt",todo)
             
    elif  whatToAcces.startswith('see'):
            todo=ReadFile("data.txt")

            # new_ToDo = []
            # for itme in todo:
            #     new_item= item.strip("\n")
            #     new_ToDo.append(new_item)

            # new_ToDo = [item.strip("\n") for item in todo]
            for id , x in enumerate(todo):
                x=x.strip("\n")
                print(f"{id+1}. {x}")
            
    elif  whatToAcces.startswith('edit'):
            try:
                todo=ReadFile("data.txt")

                edit=int(whatToAcces[5:])
                edit=edit-1

                if(todo[edit]!=None):
                    var=input("Change to what?: ")
                    todo[edit]=var+"\n"

                WriteFile("data.txt",todo)
            except ValueError:
                 print("Command not valid")
                 continue
            except:
                print("Something else went wrong or number does not exist")
                continue
            
                    
    elif whatToAcces.startswith('exit'):
            break
    else:
            print("No such option")
        
