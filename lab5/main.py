# /// script
# dependencies = ["toolz==1.2.0"]
# ///
from toolz.curried import cons, filter, map, merge_with, reduce


STUDENTS = (
    {"name": "Анна", "age": 20, "grade": 4.5},
    {"name": "Борис", "age": 22, "grade": 3.8},
    {"name": "Виктор", "age": 19, "grade": 4.2},
    {"name": "Галина", "age": 21, "grade": 4.9},
    {"name": "Дмитрий", "age": 23, "grade": 3.5},
)

# уровень 1
GRADE_LINES = map(
    lambda student: f"Имя: {student['name']}, Оценка: {student['grade']}"
)

# уровень 2
ABOVE_FOUR = filter(lambda student: student["grade"] > 4.0)

# уровень 3
# Каждый студент добавляет свой возраст к сумме и единицу к количеству.
AGE_COUNTS = map(lambda student: {"total": student["age"], "count": 1})
MEAN = lambda total: lambda count: total / count if count else None

# cons ставит нулевые суммы в начало. merge_with(sum) складывает одноимённые поля.
AGE_TOTALS = lambda students: reduce(merge_with(sum))(
    cons({"total": 0, "count": 0})(AGE_COUNTS(students))
)

# Только вызов второй лямбды запускает reduce и чтение отобранных записей.
AVERAGE_AGE_ABOVE_FOUR = lambda students: lambda: (
    lambda totals: MEAN(totals["total"])(totals["count"])
)(AGE_TOTALS(ABOVE_FOUR(students)))


def main():
    print("Уровень 1. Все студенты")
    print("\n".join(GRADE_LINES(STUDENTS)))
    print("\nУровень 2. Оценка выше 4.0")
    print("\n".join(GRADE_LINES(ABOVE_FOUR(STUDENTS))))
    print("\nУровень 3. Средний возраст отобранных студентов")
    print(AVERAGE_AGE_ABOVE_FOUR(STUDENTS)())


if __name__ == "__main__":
    main()
