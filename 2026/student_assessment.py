# student assessment 
# PF3
# Sam M 16-Feb-2026




def get_student_details():
    name = input("Enter your name (first & last): ")
    results = int(input("Enter your assessment results: "))
    max_possible = int(input("What is the possible mark? "))
    return name, results, max_possible

# Main
test = True
while test:
    student_name, score, possible_marks = get_student_details()
    print(f"Your name: {student_name}")
    percentage = score / possible_marks * 100
    percentage_rounded = round(percentage, 0)

    if percentage < 50 and percentage >= 0:
        print("You failed the assessment, please re-do it.")
        print(f"Your percentage score: {int(percentage_rounded)}%")
        test = False
    elif percentage >= 50 and percentage <= 100:
        print("Well done. You passed the assessment.")
        print(f"Your percentage score: {int(percentage_rounded)}%")
        test = False
    else:
        print("Please enter a valid score.")