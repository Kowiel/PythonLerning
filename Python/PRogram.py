import time

print("Your To do list: \n")

while True:
    print("Would you like to add, remove or see an item add remove see o exit: \n")
    whatToAcces =  input()
    whatToAcces= whatToAcces.strip()
    if whatToAcces.startswith('add'):
            item = whatToAcces.replace('add ','',1)+"\n"
            item=item.title()

            with open("data.txt","r") as file:
                todo=file.readlines()

            todo.append(item) 

            with open("data.txt","w") as file:
                file.writelines(todo)

    elif whatToAcces.startswith('remove'):
             item =  int(whatToAcces[7:])
             item-=1

             with open("data.txt","r") as file:
                todo=file.readlines()  
             
             print(f"removed the task {todo[item]}")
             todo.pop(item)

             with open("data.txt","w") as file:
                file.writelines(todo)
             
    elif  whatToAcces.startswith('remove'):
            with open("data.txt","r") as file:
             todo=file.readlines()

            # new_ToDo = []
            # for itme in todo:
            #     new_item= item.strip("\n")
            #     new_ToDo.append(new_item)

            # new_ToDo = [item.strip("\n") for item in todo]
            for id , x in enumerate(todo):
                x=x.strip("\n")
                print(f"{id+1}. {x}")
            
    elif  whatToAcces.startswith('edit'):
            with open("data.txt","r") as file:
             todo=file.readlines()

            edit=int(input(whatToAcces[5:]))
            edit=edit-1

            if(todo[edit]!=None):
                var=input("Change to what?: ")
                todo[edit]=var+"\n"

            with open("data.txt","w") as file:
                file.writelines(todo)
                
    elif whatToAcces.startswith('exit'):
            break
    else:
            print("No such option")
        
