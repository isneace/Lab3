"""
Developer: Isaac Neace
Program: Hashing Algorithm (Modulo Division)

Date: 9/13/2018
Description: Uses a hashing algorithm to sort data to make it easier to find for the computer.

PsuedoCode:
Create empty list
Fill list values with .dat index
Use Modulo hashing to convert key to address
for each collision use a quadratic or linear solution to re-asign the address
prompt user to search using a key
Take average of values in user search
Find max of list of values for user search
"""

MaxIndex = 17389              #Variable that limits how big the list can get

HashTable = [None] * MaxIndex #Creates a list with blank index's


collisions = 0                #Variable for how many times there are duplicate addresses
k = 0
probe = 0

#Below reads .dat file and converts to list
fp = open("Annual_Snow_Falls.dat", "r") 
line = fp.readline()
while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    field = line.split()
    key = int(field[1])
    address = key % MaxIndex #Creates an address based off the key

    if HashTable[address] != None:
        collisions += 1 #Counts number of collisions (where there are duplicate addresses)
    i = 0
    while HashTable[address] != None and address < MaxIndex: #Reacts if there are duplicate addresses by making a new address)
        k += 1
        i += 1
        #address += 1
        address += i**2
        probe += 1

    if HashTable[address] != None or address >= MaxIndex: #Exit if there are no more available probes
        exit()

    else:
        HashTable[address] = field
        

print("Number of Collisions: ", collisions) 
print("Number of Probes: ", probe)
    
key = input("Enter Key: ")
address = key % MaxIndex #Converts user input to address for optimal search

print(address)

#Avg = (float(address[2]) + float(address[3]) + float(address[4]) + float(address[5]) + float(address[6])) / 4.0

snowMax = []
snowMax.append(float(HashTable[address[2]]))
snowMax.append(float(HashTable[address[3]]))
snowMax.append(float(HashTable[address[4]]))
snowMax.append(float(HashTable[address[5]]))
snowMax.append(float(HashTable[address[6]]))

Max = max(snowMax)

print("The maximum value: ", Max)
print("The average value is: ", Avg)
"""
Ouput:
97004
Max(45.2)
Avg(32.5)
Ouput:

"""

