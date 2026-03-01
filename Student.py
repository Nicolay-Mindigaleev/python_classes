class Student:
    name: str
    group: int | str
    grades: dict[str, int]
    def __init__(self, name: str, group: int | str, grades: dict[str, int]) -> None:
        self.name = name
        self.group = group
        self.grades = {}
        self.grades.update(grades)
    def average_grade_of_student(self) -> float:
        sum_grades = 0
        for i in self.grades:
            sum_grades += self.grades[i]
        return sum_grades / len(self.grades)
def average_grade_of_group(student_list: list[Student], group: int | str) -> float | None:
    sum_grades = 0
    count_students = 0
    for i in student_list:
        if i.group == group:
            sum_grades += i.average_grade_of_student()
            count_students += 1
    if count_students > 0:
        return sum_grades / count_students
    return None
def average_grade_of_subject(student_list: list[Student], group: int | str, subject: str) -> float | None:
    sum_grades = 0
    count_students = 0
    for i in student_list:
        if i.group == group and subject in i.grades:
            sum_grades += i.grades[subject]
            count_students += 1
    if count_students > 0:
        return sum_grades / count_students
    return None
def create_scholarship_students_list(student_list: list[Student]) -> list[str]:
    scholarship_students_list = []
    for i in student_list:
        great_grades = True
        for j in i.grades:
            if i.grades[j] < 4:
                great_grades = False
                break
        if great_grades:
            scholarship_students_list.append(i.name)
    return scholarship_students_list
def create_expulsion_list(student_list: list[Student]) -> list[str]:
    expulsion_list = []
    for i in student_list:
        count_twos = 0
        for j in i.grades:
            if i.grades[j] <= 2:
                count_twos += 1
        if count_twos >= 3: #Пусть для отчисления нужно будет получить 3 двойки
            expulsion_list.append(i.name)
    return expulsion_list
students = [
    Student("Alice Johnson", 101, {"math": 5, "physics": 4, "chemistry": 5, "history": 4, "english": 5}),
    Student("Bob Smith", 101, {"math": 3, "physics": 3, "chemistry": 4, "history": 4, "english": 3}),
    Student("Charlie Brown", 101, {"math": 4, "physics": 5, "chemistry": 4, "history": 5, "english": 4}),
    Student("Diana Prince", 101, {"math": 5, "physics": 5, "chemistry": 5, "history": 5, "english": 5}),
    
    Student("Eve Adams", 102, {"math": 4, "physics": 4, "chemistry": 4, "history": 4, "english": 4}),
    Student("Frank Castle", 102, {"math": 3, "physics": 3, "chemistry": 2, "history": 3, "english": 3}),
    Student("Grace Hopper", 102, {"math": 5, "physics": 5, "chemistry": 5, "history": 4, "english": 5}),
    Student("Hank Pym", 102, {"math": 4, "physics": 5, "chemistry": 3, "history": 4, "english": 4}),
    
    Student("Ivy League", 103, {"math": 2, "physics": 2, "chemistry": 3, "history": 2, "english": 3}),
    Student("Jack Sparrow", 103, {"math": 3, "physics": 4, "chemistry": 4, "history": 5, "english": 4}),
    Student("Kelly Jones", 103, {"math": 5, "physics": 4, "chemistry": 5, "history": 5, "english": 5}),
    Student("Leo Messi", 103, {"math": 4, "physics": 3, "chemistry": 4, "history": 3, "english": 4}),
]
print(f"Alice Johnson average grades: {students[0].average_grade_of_student()}")
print(f"Average grades in 101 group: {average_grade_of_group(students, 101)}")
print(f"Average grades in 102 group: {average_grade_of_group(students, 102)}")
print(f"Average grades in 103 group: {average_grade_of_group(students, 103)}")
print(f"Average grades in 101 group in history: {average_grade_of_subject(students, 101, "history")}") 
print(f"scholarship students list: {create_scholarship_students_list(students)}")
print(f"expulsion list: {create_expulsion_list(students)}")
