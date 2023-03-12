from datetime import datetime
import Functions #could also as Func

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(f"Your To do list It is: {dt_string} \n")

while True:
    print("Would you like to add, remove or see an item add remove see o exit: \n")
    whatToAcces =  input()
    whatToAcces= whatToAcces.strip()
    if whatToAcces.startswith('add'):
            item = whatToAcces.replace('add ','',1)+"\n"
            item=item.title()

            todo=Functions.ReadFile("data.txt")

            todo.append(item) 

            Functions.WriteFile("data.txt",todo)

    elif whatToAcces.startswith('remove'):
             item =  int(whatToAcces[7:])
             item-=1

             todo=Functions.ReadFile("data.txt")
             
             print(f"removed the task {todo[item]}")
             todo.pop(item)

             Functions.WriteFile("data,txt",todo)
             
    elif  whatToAcces.startswith('see'):
            todo=Functions.ReadFile("data.txt")

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
                todo=Functions.ReadFile("data.txt")

                edit=int(whatToAcces[5:])
                edit=edit-1

                if(todo[edit]!=None):
                    var=input("Change to what?: ")
                    todo[edit]=var+"\n"

                Functions.WriteFile("data.txt",todo)
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