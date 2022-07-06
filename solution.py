import os

BASE_DIR = os.getcwd() 

with open(BASE_DIR+ "\\advent-day1-part2\\input.txt") as File :
    File = File.readlines()
File = [ l.strip() for l in File ] 
File = [int(x) for x in File]
Inputs = []
for x in range(2,len(File)) :
    Input = File[x-2] + File[x-1] + File[x] 
    Inputs.append(Input)
# print(Inputs)
increment = 0
for x in range(1,len(Inputs)) :
    if Inputs[x] > Inputs[x-1] :
        increment += 1
print(increment)

