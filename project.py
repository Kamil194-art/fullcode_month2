with open("user.txt", "w") as file:
    file.write("Islam 5 4 5\n")
    file.write("Kanimet 3 4 4\n")
    file.write("Kelsinai 5 5 5\n")
students = []
with open("user.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        name = parts[0]
        grades = list(map(int, parts[1:]))

        average = sum(grades) / len(grades)
        students.append((name, average))
students.sort(key=lambda x: x[1], reverse=True)
for student in students:
    print(student[0], "- средний балл:", round(student[1], 2))

