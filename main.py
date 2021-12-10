class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        sum_grades = 0
        num_lections = 0
        for lection in self.courses_in_progress:
            sum_grades += sum(self.grades[lection])
            num_lections += len(self.grades[lection])
        for lection in self.finished_courses:
            sum_grades += sum(self.grades[lection])
            num_lections += len(self.grades[lection])
        res = round(sum_grades / num_lections, 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.avg_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Можно сравнивать только студентов')
            return
        return self.avg_grade() < other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        sum_grades = 0
        num_lections = 0
        for lection in self.courses_attached:
            sum_grades += sum(self.grades[lection])
            num_lections += len(self.grades[lection])
        res = round(sum_grades / num_lections, 1)
        return res

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.avg_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Можно сравнивать только лекторов')
            return
        return self.avg_grade() < other.avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res



student_1 = Student('Konstantin', 'Ponamorev', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['GIT']
student_1.finished_courses += ['Pascal']

student_2 = Student('Svetlana', 'Ivanova', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Pascal']
student_2.finished_courses += ['GIT']

lector_1 = Lecturer('Oleg', 'Bulygin')
lector_1.courses_attached += ['Python']
lector_1.courses_attached += ['Pascal']

lector_2 = Lecturer('Ivan', 'Ivanov')
lector_2.courses_attached += ['GIT']
lector_2.courses_attached += ['Pascal']

reviewer_1 = Reviewer('Yan', 'Sidorov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['GIT']

reviewer_2 = Reviewer('Vladimir', 'Vladimirov')
reviewer_2.courses_attached += ['Pascal']
reviewer_2.courses_attached += ['GIT']



student_1.rate_lection(lector_1, 'Python', 10)
student_1.rate_lection(lector_1, 'Python', 9)
student_1.rate_lection(lector_1, 'Python', 10)

student_1.rate_lection(lector_1, 'Pascal', 7)
student_1.rate_lection(lector_1, 'Pascal', 9)
student_1.rate_lection(lector_1, 'Pascal', 9)

student_1.rate_lection(lector_2, 'GIT', 7)
student_1.rate_lection(lector_2, 'GIT', 9)
student_1.rate_lection(lector_2, 'GIT', 8)

student_1.rate_lection(lector_2, 'Pascal', 5)
student_1.rate_lection(lector_2, 'Pascal', 6)
student_1.rate_lection(lector_2, 'Pascal', 6)

student_2.rate_lection(lector_1, 'Python', 9)
student_2.rate_lection(lector_1, 'Python', 9)
student_2.rate_lection(lector_1, 'Python', 10)

student_2.rate_lection(lector_1, 'Pascal', 9)
student_2.rate_lection(lector_1, 'Pascal', 8)
student_2.rate_lection(lector_1, 'Pascal', 8)

student_2.rate_lection(lector_2, 'GIT', 6)
student_2.rate_lection(lector_2, 'GIT', 6)
student_2.rate_lection(lector_2, 'GIT', 7)

student_2.rate_lection(lector_2, 'Pascal', 5)
student_2.rate_lection(lector_2, 'Pascal', 4)
student_2.rate_lection(lector_2, 'Pascal', 5)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_1, 'GIT', 10)
reviewer_1.rate_hw(student_1, 'GIT', 10)
reviewer_1.rate_hw(student_1, 'GIT', 10)

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_1.rate_hw(student_2, 'GIT', 8)
reviewer_1.rate_hw(student_2, 'GIT', 9)
reviewer_1.rate_hw(student_2, 'GIT', 8)

reviewer_2.rate_hw(student_1, 'GIT', 10)
reviewer_2.rate_hw(student_1, 'GIT', 10)
reviewer_2.rate_hw(student_1, 'GIT', 10)

reviewer_2.rate_hw(student_1, 'Pascal', 10)
reviewer_2.rate_hw(student_1, 'Pascal', 10)
reviewer_2.rate_hw(student_1, 'Pascal', 10)

reviewer_2.rate_hw(student_2, 'GIT', 9)
reviewer_2.rate_hw(student_2, 'GIT', 7)
reviewer_2.rate_hw(student_2, 'GIT', 6)

reviewer_2.rate_hw(student_2, 'Pascal', 9)
reviewer_2.rate_hw(student_2, 'Pascal', 8)
reviewer_2.rate_hw(student_2, 'Pascal', 8)





# cool_reviewer = Reviewer('Some', 'Buddy')
# cool_reviewer.courses_attached += ['GIT']
# cool_reviewer.courses_attached += ['Python']










# cool_lector = Lecturer('Oleg', 'Bulygin')
# cool_lector.courses_attached += ['Python']

# best_student.rate_lection(cool_lector, 'Python', 10)
# best_student.rate_lection(cool_lector, 'Python', 10)
# best_student.rate_lection(cool_lector, 'Python', 10)

# cool_reviewer.rate_hw(best_student, 'GIT', 10)
# cool_reviewer.rate_hw(best_student, 'GIT', 9)
# cool_reviewer.rate_hw(best_student, 'GIT', 8)
# cool_reviewer.rate_hw(best_student, 'Python', 9)
# cool_reviewer.rate_hw(best_student, 'Python', 9)
# cool_reviewer.rate_hw(best_student, 'Python', 9)
#
# print(best_student)


# print(cool_lector)
# print(best_student.grades)
# print(cool_lector.grades)