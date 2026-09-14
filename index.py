print("================================")
print("    STUDENT MARKS ANALYZER")
print("================================")
import numpy as np
num1=input("Enter Student Name:")
roll=input("Enter Roll Number:") 
sub=["Python","DBMS","AI/ML","Computer Networks","Java"]
marks=[]
for subjects in sub:
    mark=int(input(f"Enter marks for {subjects}:"))
    marks.append(mark)

marks=np.array(marks)
print()

print("--------------Student Marks----------------")
print()
print("Student Name:",num1)
print("Roll Number:",roll)
print()
for i in range(len(sub)):
    print(sub[i],":",marks[i])
print()

print("----------Result-----------")
print()
print("Student Name:",num1)
print("Roll Number:",roll)
print()
print("Total Marks:",np.sum(marks),"/ 500")
print("average Marks:",np.mean(marks))
print("Highest Marks:",np.max(marks))
print("Lowest Marks:",np.min(marks))

percentage = (np.sum(marks) / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if np.all(marks >= 33):
    result = "PASS"
else:
    result = "FAIL"

print("Percentage :", percentage, "%")
print()


print("Grade      :", grade)
print("Result     :", result)

