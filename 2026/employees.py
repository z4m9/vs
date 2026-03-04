""" Employee Dataclasses
PF 5.6
Samuel Marriott 3/03/2026 """

from dataclasses import dataclass
@dataclass

class employee():
    firstName: str
    surname: str
    employeeID: int
    payrate: float

classArray = [employee("", "", x + 1, 0) for x in range(6)]
print(classArray)

classArray[0] = employee("Kerry", "Jones", 31532, 7.85)
print(classArray[0])


#"""Employee Records
classArray[0] = employee("Jones", "Kerry", 31532, 7.85)
classArray[1] = employee("McAllister", "David", 93420, 8.30)
classArray[2] = employee("Nguyen", "Tran", 29486, 7.40)
classArray[3] = employee("Hussein", "Wasim", 94756, 7.85)
classArray[4] = employee("Davis", "Mary", 45820, 8.00)
classArray[5] = employee("Schmidt", "Heidi", 61922, 7.60)

#print(classArray[0].name, "'s class is", classArray[0].regclass)

"""for x in range(len(classArray)):
    #print("What is employee", classArray[x].employeeID, "Name?")
    #classArray[x].name = input("Enter name here: ")"""

for x in range(len(classArray)):
    print(f"Employee {x + 1} details: \n First name:", classArray[x].firstName,
           "\n Surname:", classArray[x].surname, "\n ID number:", classArray[x].employeeID,
             "\n Pay rate: $", classArray[x].payrate)