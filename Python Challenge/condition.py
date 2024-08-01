score = float(input("Enter the student's score (0-100): "))

if score == 100:
    print("Perfect score!")
if score >= 60:
    print("You passed the course.")
else:
    print("You did not pass the course.")
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F' 

print(f"Grade: {grade}")
if grade == 'A':
    if score == 100:
        feedback += " Perfect score!"
elif grade == 'B':
    if score >= 90 and score < 95:
        feedback += " You're close to a perfect score, keep it up!"
elif grade == 'C':
    feedback = "You passed, but there's room for improvement."
elif grade == 'D':
    feedback = "You barely passed. Consider studying more."
else:
    feedback = "You failed. Better luck next time."

print(feedback) 



