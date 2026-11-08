# Author:Takalani Emmanuel Singo
# 1st git-hub project
# student grade calculator

print("_______Grade-Calculator_______")
print()
course = input("Enter course name:\n")
# check your course website for weightings/percentages

# Class record calculation
n = int(input("How many CR components does the course have:\n")) #how many are Things that make up your class record

Class_record = 0
total_weight = 0

for i in range(n):
    print(f"\n--- Component {i+1} ---")
    name = input("Enter CR component:\n") # name of the thing that makes up your class record
    mark = float(input(f"Enter {name} Mark:\n")) # Mark you got
    total = float(input(f"Enter {name} Total:\n")) # Total Mark
    weight = float(input(f"Enter {name} percentage weighting in CR:\n")) #Weighting percentages

    percent = (mark / total) * 100
    Class_record += (weight / 100) * percent
    total_weight += weight

if total_weight != 100:
    print("CR weightings should add up to 100")

print(f"\nYour Class record for {course} is: {Class_record:.2f}") #Your class record for the course

# Final Semester mark calculation
w_exam = float(input("\nExam % weighting in FINAL mark:\n"))
Exam_Total = float(input("Enter Exam Total:\n"))

has_written = input("Have you written the exam yet? (yes/no):\n").lower().strip()

if has_written == "yes":
    Exam = float(input("Enter Exam Mark:\n"))
    exam_percent = (Exam / Exam_Total) * 100
    Final_Mark = ((1 - w_exam/100) * Class_record) + ((w_exam/100) * exam_percent)
    print(f"\nYour Final Semester Mark is: {Final_Mark:.2f}")

    # Subminimum check
    if exam_percent < 40:
        print("You did not meet the 40% exam subminimum, so you fail.")
    elif Final_Mark >= 50:
        print("You passed!")
    else:
        print("You did not reach 50% for the final mark.")

else:
    Final_Mark = ((1 - w_exam/100) * Class_record)
    print(f"\nYou haven't written exam yet.")
    print(f"Your Final Mark so far (exam = 0) is: {Final_Mark:.2f}")

    need_for_50 = (50 - Final_Mark) / (w_exam/100)

    # impossibility check
    if need_for_50 > 100:
        print(f"\nYou need {need_for_50:.2f}% on exam to get 50% final")
        print("That's over 100% - so 50% final is no longer possible.")
        print("Focus on getting 40%+ to meet subminimum and try for a supplementary.")
    else:
        print(f"\nTo get 50% final, you need {need_for_50:.2f}% on exam")
        print(f"To meet subminimum, you need at least 40% on exam")
        print(f"So your REAL target is {max(need_for_50, 40):.2f}% on exam")
