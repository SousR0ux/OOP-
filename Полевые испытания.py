# Класс Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод для вывода информации о студенте
    def __str__(self):
        average_grade = self.get_average_grade()
        return (f"Student: {self.name} {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    # Метод для выставления оценки лектору
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 <= grade <= 10:
                if course in lecturer.lecturer_grades:
                    lecturer.lecturer_grades[course].append(grade)
                else:
                    lecturer.lecturer_grades[course] = [grade]
            else:
                print("Ошибка: Оценка должна быть в диапазоне от 0 до 10")
        else:
            print("Ошибка: Лектор не ведет данный курс или студент не записан на курс")

    # Метод для получения средней оценки
    def get_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    # Перегрузка оператора сравнения
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка: Сравнение возможно только между студентами")
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

# Родительский класс Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Дочерний класс Lecturer, наследующийся от Mentor
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    # Метод для получения средней оценки
    def get_average_grade(self):
        all_grades = [grade for grades in self.lecturer_grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    # Метод для вывода информации о лекторе
    def __str__(self):
        average_grade = self.get_average_grade()
        return (f"Lecturer: {self.name} {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade:.1f}")

    # Перегрузка оператора сравнения
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка: Сравнение возможно только между лекторами")
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()

# Дочерний класс Reviewer, наследующийся от Mentor
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод для проверки домашних заданий
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print("Ошибка: Оценка должна быть в диапазоне от 0 до 10")
        else:
            print('Ошибка')

    # Метод для вывода информации о ревьюере
    def __str__(self):
        return f"Reviewer: {self.name} {self.surname}\nИмя: {self.name}\nФамилия: {self.surname}"

# Функция для подсчета средней оценки за домашние задания по всем студентам
def get_average_grade_for_students(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0

# Функция для подсчета средней оценки за лекции по всем лекторам
def get_average_grade_for_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.lecturer_grades:
            all_grades.extend(lecturer.lecturer_grades[course])
    return sum(all_grades) / len(all_grades) if all_grades else 0

# Пример использования классов

# Создаем студентов
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Jane', 'Doe', 'female')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

# Создаем лекторов
lecturer1 = Lecturer('Anna', 'Petrova')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('John', 'Smith')
lecturer2.courses_attached += ['Python']

# Создаем экспертов (ревьюеров)
reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Alice', 'Johnson')
reviewer2.courses_attached += ['Python']

# Эксперты проверяют домашние задания студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 7)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 7)

# Вывод информации о студентах, лекторах и ревьюерах
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Подсчет и вывод средней оценки за домашние задания по всем студентам
average_student_grade = get_average_grade_for_students([student1, student2], 'Python')
print(f"Средняя оценка за домашние задания по курсу 'Python': {average_student_grade:.1f}")

# Подсчет и вывод средней оценки за лекции по всем лекторам
average_lecturer_grade = get_average_grade_for_lecturers([lecturer1, lecturer2], 'Python')
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecturer_grade:.1f}")
