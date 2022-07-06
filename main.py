 class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _avg_rate_hw(self):
        sum_hw = 0
        count = 0
        for grade in self.grades.values():
            sum_hw += grade
            count += len(grade)
        return round(sum_hw / count, 2)

    def __str__(self):
        string = f'Имя: {self.name} \n' \
                  f'Фамилия: {self.surname} \n' \
                  f'Средняя оценка за домашнее задание: {self._avg_rate_hw()} \n' \
                  f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)} \n' \
                  f'Завершённые курсы: {" ".join(self.finished_courses)} \n'
        return string

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента не существует')
            return
        else:
            compare = self._avg_rate_hw() < other_student._avg_rate_hw()
            if compare:
                f'{self.name}, {self.surname} учится хуже чем {other_student.name}, {other_student.surname}'
            else:
                f'{self.name}, {self.surname} учится лучше чем {other_student.name}, {other_student.surname}'
            return compare

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Error')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avr_lec_rate(self):
        sum_lect = 0
        count_len = 0
        for grade in self.grades.values():
            sum_lect += grade
            count_len += len(grade)
        return round(sum_lect / count_len, 2)

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора не существует.')
            return
        else:
            compare = self.avr_lec_rate() < other_lecturer.avr_lec_rate()
            if compare:
                f'{self.name}, {self.surname} учится хуже чем {other_lecturer.name}, {other_lecturer.surname}'
            else:
                f'{self.name}, {self.surname} учится лучше чем {other_lecturer.name}, {other_lecturer.surname}'
            return compare

    def __str__(self):
        string_g = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {avr_lec_rate()}'
        return string_g


class Reviewer(Mentor):
    def __str__(self):
        string = f'Имя: {self.name} \nФамилия: {self.surname}'
        return string

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def get_avg_rate_hw_by_course(l_students, course):
    sum_ = 0
    for student in l_students:
        for course_, grades in student.grades.items():
            if course_ == course:
                sum_ += sum(grades) / len(grades)
    return sum_


def get_avg_rate_lecture_by_course(l_lecturer, course):
    sum_ = 0
    for lecturer in l_lecturer:
        for course_, grades in lecturer.grades.items():
            if course_ == course:
                sum_ += sum(grades) / len(grades)
    return sum_