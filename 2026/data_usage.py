# This program allows users to understand their data consumption and if they are close to reaching their limit.

#asks the user how much mobile data is included in their plan (in gigabytes)
#asks the user how much data they have used so far (in gigabytes)
# Cast as number
#calculates how much data the user has remaining
# Calculate the amount remaining by subtracting the amount consumed from the original amount.
#displays a clear message showing the result

starting_allowance = int(input("How much GB of data is in your plan? "))
amount_used = int(input("How much GB of data have you consumed? "))
remaining_amount = starting_allowance - amount_used
print(f"You have {remaining_amount} GB of data remaining.")