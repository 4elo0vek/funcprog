from functools import reduce


STUDENTS = (
    {"name": "Анна", "age": 20, "grade": 4.5},
    {"name": "Борис", "age": 22, "grade": 3.8},
    {"name": "Виктор", "age": 19, "grade": 4.2},
    {"name": "Галина", "age": 21, "grade": 4.9},
    {"name": "Дмитрий", "age": 23, "grade": 3.5},
)

# уровень 1
GRADE_LINES = lambda students: map(
    lambda student: f"Имя: {student['name']}, Оценка: {student['grade']}",
    students,
)

# уровень 2
ABOVE_FOUR = lambda students: filter(lambda student: student["grade"] > 4.0, students)

# уровень 3
MEAN = lambda total, count: total / count if count else None

AVERAGE_AGE_ABOVE_FOUR = lambda students: lambda: MEAN(
    *reduce(
        lambda totals, student: (totals[0] + student["age"], totals[1] + 1),
        ABOVE_FOUR(students),
        (0, 0),
    )
)


print("Уровень 1. Все студенты", *GRADE_LINES(STUDENTS), sep="\n")
print("\nУровень 2. Оценка выше 4.0", *GRADE_LINES(ABOVE_FOUR(STUDENTS)), sep="\n")
print("\nУровень 3. Средний возраст отобранных студентов", AVERAGE_AGE_ABOVE_FOUR(STUDENTS)(), sep="\n")

