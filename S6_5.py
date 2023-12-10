subj = ('Русский', 'Английский', 'Математика')

grades = [
    (46, 95, 37),
    (90, 89, 91),
    (90, 35, 99)
]

def average_grades(student_grades):
    num_subj = len(subj)
    total = sum(student_grades)
    return total / num_subj


student1_average = average_grades(grades[0])
print(f"Средний балл студента №1: {student1_average}")

student2_average = average_grades(grades[1])
print(f"Средний балл студента №2: {student2_average}")

student3_average = average_grades(grades[2])
print(f"Средний балл студента №3: {student3_average}")