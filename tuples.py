# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Nguyen", 21, "male")

print(student.count("Nguyen"))
print(student.index("male"))

for x in student:
    print(x)

if "Nguyen" in student:
    print("Nguyen is here!")