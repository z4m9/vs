""" Employee Dataclasses
PF 5.6
Samuel Marriott 3/03/2026 """

from dataclasses import dataclass
@dataclass

class employee():
    name: str
    regclass: str
    employeeID: int

classArray = [employee("", "", x + 1) for x in range(5)]
print(classArray)

classArray[0] = employee("Steve", "1D1", 1)
print(classArray[0])

#print(classArray[0].name, "'s class is", classArray[0].regclass)


for x in range(len(classArray)):
    print("What is employee", classArray[x].employeeID, "Name?")
    classArray[x].name = input("Enter name here: ")

for x in range(len(classArray)):
    print("Employee", str(classArray[x].employeeID), "is", classArray[x].name)