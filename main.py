name = input("Enter your name: ")
section = input("Enter your section: ")

if section == 'K' or section == 'I':
    if len(name) % 2 == 0:
        category = "Good"
    else:
        category = "None"
else:
    category = "None"

n = int(input("Enter number of students: "))

v_count = 0
f_count = 0

for i in range(n):
    mark = int(input("Enter marks of student " + str(i + 1) + ": "))

    if category == "Good" and mark >= 60 and mark <= 74:
        mark = mark + 3

    if mark < 0 or mark > 100:
        print(mark, "-> The marks are Invalid")

    elif mark >= 90 and mark <= 100:
        print(mark, "-> The marks are Excellent")
        v_count += 1

    elif mark >= 75 and mark <= 89:
        print(mark, "-> The marks are Very Good")
        v_count += 1

    elif mark >= 60 and mark <= 74:
        print(mark, "-> The marks are Good")
        v_count += 1

    elif mark >= 40 and mark <= 59:
        print(mark, "-> The marks are Average")
        v_count += 1

    else:
        print(mark, "-> Fail")
        f_count += 1

print("Total Passed Students:", v_count)
print("Total Failed Students:", f_count)
