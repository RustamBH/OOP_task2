class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
# best_student.courses_in_progress += ['C++']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
# cool_reviewer.courses_attached += ['C++']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
print(best_student.grades)


best_lecturer = Lecturer('Sam', 'Thomson')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['C++']

best_student.rate_hw(best_lecturer, 'Python', 8)
best_student.rate_hw(best_lecturer, 'Python', 9)
best_student.rate_hw(best_lecturer, 'Python', 10)

best_student.rate_hw(best_lecturer, 'C++', 6)
best_student.rate_hw(best_lecturer, 'C++', 7)
best_student.rate_hw(best_lecturer, 'C++', 8)

print(best_lecturer.grades)