marks=[78,85,46,92,63]
total=0
passed=0

for mark in marks:
    total=total+mark

    if mark>=50:
        passed=passed+1

average=total/len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Passed courses:", passed)