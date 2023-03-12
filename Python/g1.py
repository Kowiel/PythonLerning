import glob
import Functions

files = glob.glob("Jornual/*.txt")

for file in files:
     Text=Functions.ReadFile(file)
     print(f"The file {file} \n contains {Text}")