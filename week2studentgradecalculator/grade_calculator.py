# Developers Arena Internship
# Week 2 Task: Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 😊"
    elif marks >= 60:
        return "D", "Needs improvement. Keep practicing 💪"
    else:
        return "F", "Don't give up! Learn and try again 🔁"


# Get student name
name = input("Enter student name: ")

# Get and validate marks
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter numbers only.")

# Calculate grade and message
grade, message = calculate_grade(marks)

# Display result
print("\nRESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
