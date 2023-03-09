import time

print("Your To do list: \n")

while True:
    print("Would you like to add, remove or see an item add remove see o exit: \n")
    whatToAcces =  input()
    whatToAcces= whatToAcces.strip()
    match whatToAcces:
        case "add":
            item = input("What item to add: ")+"\n"
            item=item.title()

            with open("data.txt","r") as file:
                todo=file.readlines()

            todo.append(item) 

            with open("data.txt","w") as file:
                file.writelines(todo)

        case "remove":
             print("What item to did you complite:")
             item =  int(input())
             item-=1

             with open("data.txt","r") as file:
                todo=file.readlines()  
             
             print(f"removed the task {todo[item]}")
             todo.pop(item)

             with open("data.txt","w") as file:
                file.writelines(todo)
             
        case "see":
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
            
        case "edit":
            with open("data.txt","r") as file:
             todo=file.readlines()

            edit=int(input("What item to eddit sepcify with number"))
            edit=edit-1

            if(todo[edit]!=None):
                var=input("Change to what?: ")
                todo[edit]=var+"\n"

            with open("data.txt","w") as file:
                file.writelines(todo)
                
        case "exit":
            break
        case _:
            print("No such option")
        
