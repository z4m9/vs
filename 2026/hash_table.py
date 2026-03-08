# PF6.5 - Hash Table
# Samuel Marriott 8/03/2026
# Questions and answers from Line 57

# Student records stored using a dictionary (hash table)
students = {
    "S001": {"name": "Alice", "age": 16, "grade": "A"},
    "S002": {"name": "Ben", "age": 17, "grade": "B"},
    "S003": {"name": "Chloe", "age": 16, "grade": "A"}
}

print("Initial student records:")
for student_id, details in students.items():
    print(student_id, ":", details)

search_id = input("\nEnter a student ID to search: ")

if search_id in students:
    print("Student found:", students[search_id])
else:
    print("Student ID not found.")

update_id = input("\nEnter student ID to update grade: ")

if update_id in students:
    new_grade = input("Enter new grade: ")
    students[update_id]["grade"] = new_grade
    print("Grade updated successfully.")
else:
    print("Student ID not found.")

delete_id = input("\nEnter student ID to delete: ")

if delete_id in students:
    del students[delete_id]
    print("Student deleted successfully.")
else:
    print("Student ID not found.")

new_id = input("\nEnter new student ID: ")

if new_id in students:
    print("This ID already exists.")
else:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

students[new_id] = {
    "name": name,
    "age": age,
    "grade": grade
    }

print("Student added successfully")

# Q1. Why is a unique ID suitable as a key in a hash table?
# A. It eliminates collisions, maximising performace.

# Q2. Why are hash tables faster than lists for searching by ID?
# A. The hash function calculates the memory location of the item, allowing faster access than linear search.

# Q3. 
# a) What is a collision in a hash table?
# A. Where two different keys generate the same index in a hash table.
# b) How might it be handled?
# A. In chaining, the colliding entries are stored in a bucket.