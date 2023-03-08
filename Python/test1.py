file = open("essay.txt","r")
Esay=file.readlines()
sum=0
# for line in Esay:
#     Line = line.split()
#     for i in Line:
#         print(i.capitalize())

for line in Esay:
    sum=sum+len(line)

print(sum)
file.close()
file = open("essay.txt", 'r')
content = file.read()

nr_chars = len(content)
print(nr_chars)
file.close()