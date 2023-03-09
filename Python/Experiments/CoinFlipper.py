totalcount=0
HeadCount=0

while True:
    flip=input("Head or Tail?:")

    if(flip=="Head"):
      HeadCount+=1
      totalcount+=1
    if(flip=="Tail"):
      totalcount+=1

    result = float((HeadCount/totalcount)*100)
    with open("Result.txt","a") as File:
       File.writelines(f"Head procentage {result} \n")
       print(f"-----Head procentage {result} ---\n")