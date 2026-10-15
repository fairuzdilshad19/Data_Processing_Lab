students=[
    {"name":"Rahim","department":"CSE",
     "marks":85,"attendance":92},
    {"name":"Karim","department":"CSE",
     "marks":48,"attendance":76},
    {"name":"Sara","department":"DS",
     "marks":91,"attendance": 95},
    {"name":"Nadia","department":"DS",
     "marks":67,"attendance": 84},
    {"name":"Hasan","department":"CSE",
     "marks":73,"attendance": 78}
]
total = 0
passed = 0

highest_mark = students[0]["marks"]
highest_student = students[0]["name"]

for student in students:
    print(student["name"],"Marks:",student["marks"])

    total=total+student["marks"]

    if student["marks"]>=50:
        passed=passed+1

    if student["marks"]>highest_mark:
        highest_mark=student["marks"]
        highest_student=student["name"]

average=total/len(students)

print("Students passed:", passed)
print("Class average:", average)
print("Highest_scoring student:", highest_student)
print("Highest mark:", highest_mark)