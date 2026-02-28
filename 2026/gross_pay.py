# gross pay
# PF 2.6
# Sam M 21-Feb-2026

#BEGIN
#SET running to true

#WHILE running is true DO
 #   FOR each employee from 1 to 3 DO
#        GET hours worked
#        GET hourly rate
#        CALCULATE gross pay
#        DISPLAY gross pay

 #       IF hours worked is greater than standard hours THEN
#            DISPLAY overtime message
 #       ENDIF
 #   END FOR

 #   ASK user if they want to run the program again
 #   IF user chooses to exit THEN
 #       SET running to false
#    ENDIF
#END WHILE

#END

running = True
employee = 3
while running:
    for employee in range(1,4):
        hours = int(input("How many hours worked? "))
        rate = int(input("What is the hourly rate of pay? "))
        gross_pay = hours * rate
        print(f"You will earn ${gross_pay}")

        if hours > 38:
            print(f"You worked overtime by {hours - 38} hours.")
        elif hours < 38:
            print(f"You need to work another {38 - hours} hours.")
        else:
            print("You worked standard hours.")
        
    user = input("Do you wish to try again? ")
    if user.lower() == "no":
        running =  False