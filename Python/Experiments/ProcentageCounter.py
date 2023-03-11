
try:
        totalValue = int(input("Put in the total amopunt"))
        curentValue = int(input("Put in the curent amopunt"))

        procentage = curentValue/totalValue*100
        print (f"The procentage is{procentage}\n")

        with open("fileProcentage.txt","a") as file:
            file.writelines(f"The procentage is{procentage}\n")
except ValueError:
        print ("Thats not a number")
except ZeroDivisionError:
        print ("Cant devide by zero")
except:
        print("Other error")