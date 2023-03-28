def round_grades(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 40:
            rounded_grades.append(grade)
        elif grade % 5 >= 3 and grade >= 40:
            rounded_grades.append((grade // 5 + 1) * 5)
        else:
            rounded_grades.append(grade)
    return rounded_grades

print(round_grades([75, 39, 82, 83, 42, 73]))