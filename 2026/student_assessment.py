def get_student_details():
    name1 = input("Enter your name (first & last): ")
    results = int(input("Enter your assessment results: "))
    max_possible = int(input("What is the possible mark? "))
    return name1, results, max_possible

# Main
student_name, score, possible_marks = get_student_details()
print(f"Your name: {student_name}")
percentage = score / possible_marks * 100

if percentage < 50 and percentage >= 0:
    print("You failed the assessment, please re-do it.")
    print(f"Your percentage score: {percentage}")
elif percentage >= 50 and percentage <= 100:
    print("Well done. You passed the assessment.")
    print(f"Your percentage score: {percentage}")
else:
    print("Please enter a valid score.")