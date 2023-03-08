import time

print("Your To do list: \n")

while True:
    print("Would you like to add, remove or see an item add remove see o exit: \n")
    whatToAcces =  input()
    whatToAcces= whatToAcces.strip()
    match whatToAcces:
        case "add":
            item = input("What item to \\add: ")+"\n"
            item=item.title()
            file = open("data.txt","r")
            todo=file.readlines()
            file.close()
            todo.append(item) 
            file = open("data.txt",'w')
            file.writelines(todo)
            file.close()
        case "remove":
             print("What item to did you complite:")
             item =  int(input())
             item-=1
             file = open("data.txt","r")
             todo=file.readlines()  
             file.close()

             todo.pop(item)

             file = open("data.txt",'w')
             file.writelines(todo)
             file.close()
        case "see":
            file = open("data.txt","r")
            todo=file.readlines()

            file.close()

            for id , x in enumerate(todo):
                print(f"{id+1}. {x} \n")
            
        case "edit":
            edit=int(input("What item to eddit sepcify with number"))
            edit=edit-1
            if(todo[edit]!=None):
                var=input("Change to what?: ")
                todo[edit]=var
        case "exit":
            break
        case _:
            print("No such option")
        
