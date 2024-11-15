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

# Пример использования классов

# Создаем студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

# Создаем лектора
cool_lecturer = Lecturer('Anna', 'Petrova')
cool_lecturer.courses_attached += ['Python']

# Создаем эксперта (ревьюера)
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Эксперт проверяет домашнее задание студента
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

# Студент оценивает лектора
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)

# Вывод информации о студенте
print(best_student)

# Вывод информации о лекторе
print(cool_lecturer)

# Вывод информации о ревьюере
print(cool_reviewer)
