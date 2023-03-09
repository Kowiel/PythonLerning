names = ["john smith", "jay santi", "eva kuki"]
printname=[name.title() for name in names]
print(printname)

usernames = ["john 1990", "alberta1970", "magnola2000"]
printname=[len(name) for name in usernames]
print(printname)

user_entries = ['10', '19.1', '20']
printname=[float(num) for num in user_entries]
print(sum(printname))

temperatures = [10, 12, 14]
 
file = open("file.txt", 'w')
printname=[str(num) + " " for num in temperatures]
file.writelines(printname)